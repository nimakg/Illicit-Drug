"""drug URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from drugapp.views import *


urlpatterns = [
     url(r'^$', home),
     url(r'^main',mainh,name="main"),
     url(r'^register',register,name='register'),
     url(r'^login',login,name='login'),
     url(r'^logout',logout,name='logout'),
     url(r'^changestate',changestate,name='changestate'),
     url(r'^uhome',uhome,name='uhome'),
     url(r'^gallery',gallery,name='gallery'),
     url(r'^upload',fileupload,name='upload'),
     url(r'^addpost',addpost,name='addpost'),
     url(r'^viewuser',viewusers,name='viewuser'),
     url(r'^viewnoti',viewnoti,name='viewnoti'),
     url(r'^addpost',addpost,name='addpost'),
     url(r'^viewposts',viewposts,name='viewposts'),
     url(r'^editupdate',editupdate,name='editupdate'),
     url(r'^updatedetails',updatedetails,name='updatedetails'),
     url(r'^download',download,name='download'),
     url(r'^graph',graph,name='graph'),
]
