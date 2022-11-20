from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('events', events, name='events'),
    path('createEvent/', createEvent, name='eventCreate'),
    path('<int:pk>/update', eventUpdate.as_view(), name='eventUpdate'),
    path('<int:pk>/delete', eventDelete.as_view(), name='eventDelete'),

    path('team/', team, name='team'),
    path('teamCreate/', teamCreate, name='teamCreate'),
    path('team/<int:pk>/update', teamUpdate.as_view(), name='teamUpdate'),
    path('team/<int:pk>/delete', teamDelete.as_view(), name='teamDelete'),

    path('sportCreate/', sportCreate, name='sportCreate'),
    path('groups/', compound, name='groups'),
    path('compoundCreate/', compoundCreate, name='compoundCreate'),
    path('organization/', organization, name='organization'),
    path('organizationСreate/', organizationСreate, name='organizationСreate'),
    path('sportObjectCreate/', sportObjectCreate, name='sportObjectCreate'),
    path('sportType/', sportType, name='sportType'),

    path('users/', users, name='users'),
    path('users/<int:pk>/update', userUpdate.as_view(), name='userUpdate'),
    path('users/<int:pk>/delete', userDelete.as_view(), name='userDelete'),
    path('UserResultCreate/', UserResultCreate, name='UserResultCreate'),
    path('UserResultCreate/<int:pk>/update', UserResultUpdate.as_view(), name='UserResultUpdate'),

]