"""sign_language_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('', views.logg),
    path('logg_post',views.logg_post),
    path('logout', views.logout),


    path('user_reg', views.user_reg),
    path('addalphabet', views.addalphabet),
    path('addalphabet_post', views.addalphabet_post),


    path('feedback', views.feedbackk),
    path('deletealpha/<id>', views.deletealpha),
    path('viewalphabet', views.viewalphabet),
    path('viewuser', views.viewuser),
    path('adminhome', views.adminhome),
    path('user_reg', views.user_reg),
    path('user_view_profile', views.user_view_profile),

    path('user_reg_post', views.user_reg_post),
    path('user_view_feedback', views.user_view_feedback),
    path('user_viewalphabet', views.user_viewalphabet),
    path('userhome', views.userhome),
    path('user_feedback',views.user_feedback),
    path('user_feedback_post', views.user_feedback_post),
    path('view_mark',views.user_view_mark),
    path('user_attend_exam',views.user_attend_exam),
    path('user_attend_exam_post',views.user_attend_exam_post),
    path('usr_view_progress',views.usr_view_progress),
    path('user_load_cam',views.user_load_cam),

]

