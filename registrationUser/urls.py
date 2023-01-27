from django.urls import path, include

from . import views
from .views import *


app_name = 'registrationUser'
urlpatterns = [
    path('', index, name='index'),
    path('login/', logIn, name='login'),
    path('logout/', logOut, name='logout'),
    path('register/', register, name='register'),
]
