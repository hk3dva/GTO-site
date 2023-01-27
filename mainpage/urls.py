from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('info', info, name='info'),
    path('smi', smi, name='smi'),
    path('partners', partners, name='partners'),
]