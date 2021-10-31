from django.contrib import admin
from django.urls import path, include

from . import views
# setting url for the app home page
urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),  # creating url for register function
    path('signin', views.signin, name="signin"),        # creating url for signin function
    path('signout', views.signout, name="signout"),     # creating url for  signout function

   ]
