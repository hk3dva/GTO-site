from django.urls import path
from .views import *

app_name = 'eventHandler'
urlpatterns = [
    path('', myEvent, name='event'),
    path('events', allEvents, name='allEvents'),
    path('createEvent/', createEvent, name='eventCreate'),
    path('SportTypeEventcreate/', SportTypeEventcreate, name='SportTypeEventcreate'),

    path('profile/<int:pk>', profile.as_view(), name='profile'),

    path('allSportsmans/', allSportsmans, name='allSportsmans'),
    path('mySportsmans/', mySportsmans, name='mySportsmans'),

    # path('<int:pk>/update', eventUpdate.as_view(), name='eventUpdate'),
    # path('<int:pk>/delete', eventDelete.as_view(), name='eventDelete'),

    path('sportCreate/', sportCreate, name='sportCreate'),
    path('sportObjectCreate/', sportObjectCreate, name='sportObjectCreate'),

    path('trainerAppoin/', trainerAppoin , name='trainerAppoin')
]