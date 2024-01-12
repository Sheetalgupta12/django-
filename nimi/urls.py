from django.contrib import admin
from django.urls import path

from .views import signuppage,loginpage,homepage,Logout

urlpatterns = [
    path('',signuppage,name="signup"),
    path('login/',loginpage,name="login"),
    path('home/',homepage,name="home"),
    path('logout/',Logout,name="logout"),
    
]