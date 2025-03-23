import random

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
import  datetime
# Create your views here.
from myapp.models import *
proj_path=r"C:\Users\aleen\Documents\sign_language_detection\sign_language_detection\\"

def logg(request):
    return render(request, "loginindex.html")

def logg_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    res=login.objects.filter(username=username,password=password)
    if res.exists():
        res1 = login.objects.get(username=username, password=password)
        request.session['lid']=0
        request.session['lid']=res1.id
        if res1.usertype == "admin":
            return HttpResponse('''<script>alert('Login Successfull');window.location="/adminhome"</script>''')
        elif res1.usertype == "user":
            return HttpResponse('''<script>alert('Login Successfull');window.location="/userhome"</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid ');window.location="/"</script>''')
    else:
         return HttpResponse('''<script>alert('User not Found');window.location="/"</script>''')

def logout(request):
    request.session['lid'] = 0

    return HttpResponse('''<script>alert('Logout Successful');window.location="/"</script>''')


def addalphabet(request):
    return render(request, "admin/addalphabet.html")


def addalphabet_post(request):
    addalphabe = request.POST['textfield']
    image=request.FILES['textfield2']
    d=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs=FileSystemStorage()
    # fs.save(proj_path + "myapp\\media\\image\\"+d+'.jpg',image)
    fs.save(r"C:\Users\aleen\Documents\sign_language_detection\sign_language_detection\media\\"+d+'.jpg',image)
    path="/media/"+d+'.jpg'
    obj=alphabet()
    obj.alphabet=addalphabe
    obj.image=path
    obj.save()
    return  HttpResponse("saved")
def deletealpha(request,id):
    alphabet.objects.filter(id=id).delete()
    return  redirect("/viewalphabet")

def feedbackk(request):
    res=feedback.objects.all()
    return render(request, "admin/feedback.html",{'data':res})


def viewalphabet(request):
    res=alphabet.objects.all()
    return render(request, "admin/viewalphabet.html",{'data':res})

def viewuser(request):
    res=user.objects.all()
    return render(request, "admin/viewuser.html",{'data':res})

def adminhome(request):
    return render(request, "admin/index.html")


# ======================
def user_reg(request):
    return render(request,"signup.html")


def user_reg_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    mob=request.POST['textfield3']
    house=request.POST['textfield4']
    post=request.POST['textfield5']
    password=request.POST['password']
    obj = login()
    obj.username = email
    obj.password = password
    obj.usertype="user"
    obj.save()
    obj1 = user()
    obj1.name = name
    obj1.email = email
    obj1.phone = mob
    obj1.house = house
    obj1.post = post
    obj1.LOGIN=obj
    obj1.save()
    return HttpResponse('''<script>alert('registered');window.location="/"</script>''')

def userhome(request):
    return render(request, "user/index.html")

def user_view_feedback(request):
        res = feedback.objects.all()
        return render(request, "user/feedback.html", {'data': res})

def user_viewalphabet(request):
        res = alphabet.objects.all()
        return render(request, "user/viewalphabet.html", {'data': res})


def user_feedback(request):
        return render(request, "user/user_feedback.html")

def user_feedback_post(request):
    feed = request.POST['textfield']
    obj2=feedback()
    obj2.feedback = feed
    obj2.USER=user.objects.get(LOGIN_id=request.session['lid'])
    obj2.date=datetime.datetime.now().strftime("%Y-%m-%d")
    obj2.save()
    return HttpResponse('''<script>alert('feedback send');window.location="/user_feedback"</script>''')

def user_view_mark(request):
    res = mark.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, "user/view_mark.html", {'data': res})


def user_view_profile(request):
    res=user.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"user/viewpage.html",{"data":res})

def user_attend_exam(request):
    lst=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    cnt=0
    qn=random.choice(lst)
    request.session['score']="0"
    request.session['selected']=qn
    print("Qn ", qn)
    return render(request, "user/attend_exam.html", {'qn':qn, "cnt":cnt, "score" : request.session['score']})


def user_attend_exam_post(request):
    cnt=request.POST["cnt"]
    correct=request.POST["correct"]
    ans=request.POST["textfield"]
    lst=["A", "B", "C", "D","E","F","G","H","I","J"]
    if correct.lower() == ans.lower():
        request.session['score'] = int(request.session['score']) + 1

    qn=random.choice(lst)
    while qn in request.session['selected']:
        qn = random.choice(lst)
    print("Qn ", qn)
    cnt = int(cnt) + 1
    if cnt<5:
        request.session['selected']=request.session['selected']+qn
        print(request.session['selected'])
        return render(request, "user/attend_exam.html", {'qn':qn, "cnt":cnt, "score":request.session['score']})
    else:
        res=mark.objects.filter(date=datetime.datetime.now().strftime("%Y-%m-%d"), USER=user.objects.get(LOGIN_id=request.session['lid']))
        if res.exists():
            res=res[0]
            res.attended = cnt
            res.correct = request.session['score']
            res.mark = request.session['score']
            res.save()
        else:
            obj=mark()
            obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
            obj.attended=cnt
            obj.correct=request.session['score']
            obj.mark=request.session['score']
            obj.USER=user.objects.get(LOGIN_id=request.session['lid'])
            obj.save()
        return HttpResponse('''<script>alert('Progress saved');window.location="/userhome"</script>''')

def usr_view_progress(request):
    res=mark.objects.filter(USER=user.objects.get(LOGIN_id=request.session['lid']))
    datelist=[]
    markslist=[]
    for i in res:
        datelist.append(i.date)
        markslist.append(int(i.mark))

    d=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # graph section
    import matplotlib.pyplot as plt
    # Create a line chart
    plt.figure(figsize=(8, 6))
    plt.plot(datelist, markslist)


    # Add title and labels
    plt.title('Your Progress')
    plt.xlabel('Attended Dates')
    plt.ylabel('Scored Marks')
    plt.savefig(proj_path + "media\\" + d + ".png")
    path="/media/" + d + ".png"
    return render(request, "user/view_progress.html", {'data':res, "path":path})

def user_load_cam(request):
    from Application_new import Application
    (Application()).root.mainloop()
    return HttpResponse('''<script>alert('Training session completed');window.location="/userhome"</script>''')
