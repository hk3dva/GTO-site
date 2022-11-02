from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', logIn, name='login'),
    path('logout/', logOut, name='logout'),
    path('register/', register, name='register'),
    path('resReg/', resReg, name='resReg'),
    path('resLog/', resLog, name='resLog'),
    path('Log/', Log, name='Log'),
    path('Event/', createEvent, name='Event'),
    path('resCreate/', resCreate, name='resCreate'),
]
