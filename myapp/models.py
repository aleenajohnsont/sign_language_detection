from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)




class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    LOGIN= models.ForeignKey(login,default=1,on_delete=models.CASCADE)



class alphabet(models.Model):
    alphabet = models.CharField(max_length=100)
    image= models.CharField(max_length=100)



class feedback(models.Model):
    date= models.CharField(max_length=100)
    feedback= models.CharField(max_length=100)
    USER= models.ForeignKey(user,default=1,on_delete=models.CASCADE)


class mark(models.Model):
     date= models.CharField(max_length=100)
     attended= models.CharField(max_length=100)
     correct = models.CharField(max_length=100)
     mark = models.CharField(max_length=100)
     USER= models.ForeignKey(user,default=1,on_delete=models.CASCADE)











