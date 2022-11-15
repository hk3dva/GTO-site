from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='event'),
    path('createEvent/', createEvent, name='eventCreate'),
    path('<int:pk>/update', eventUpdate.as_view(), name='eventUpdate'),
    path('<int:pk>/delete', eventDelete.as_view(), name='eventDelete'),

    path('teamCreate/', teamCreate, name='teamCreate'),
    path('team/<int:pk>/update', teamUpdate.as_view(), name='teamUpdate'),
    path('team/<int:pk>/delete', teamDelete.as_view(), name='teamDelete'),

    path('sportCreate/', sportCreate, name='sportCreate'),
    path('compoundCreate/', compoundCreate, name='compoundCreate'),
    path('organizationСreate/', organizationСreate, name='organizationСreate'),
    path('sportObjectCreate/', sportObjectCreate, name='sportObjectCreate'),
    path('UserResultCreate/', UserResultCreate, name='UserResultCreate'),
    path('UserResultCreate/<int:pk>/update', UserResultUpdate.as_view(), name='UserResultUpdate'),

]