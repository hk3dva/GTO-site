from django.urls import path, include

from .views import *


app_name = 'registrationUser'
urlpatterns = [
    path('', index, name='index'),
    path('logout/', logOut, name='logout'),
    path('register/', register, name='register'),
]
