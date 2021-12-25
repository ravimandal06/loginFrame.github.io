# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.index, name=""),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout")
]
