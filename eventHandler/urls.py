from django.urls import path
from .views import *

app_name = 'eventHandler'
urlpatterns = [
    path('sportCreate/', sportCreate, name='sportCreate'), # Создание вида спорта
    path('sportObjectCreate/', sportObjectCreate, name='sportObjectCreate'), # Создание спортивного объекта
    path('sportObjectSettings/<int:pk>', sportObjectSettings, name='sportObjectSettings'), # Настройка спортивного объекта
    path('profile/<int:pk>', profile.as_view(), name='profile'), # Страница пользователя для каждого пользователя уникальна
    path('createEvent/', createEvent, name='eventCreate'), # Создание мероприятия
    path('trainerAppoin/', trainerAppoin , name='trainerAppoin'), # Назначить пользователя тренером
    path('organizerAppoin/', organizerAppoin , name='organizerAppoin'), # Назначить пользователя тренером
    path('allSportsmans/', allSportsmans, name='allSportsmans'), # Список всех спортсменов
    path('TrainerSportsmans/', mySportsmans, name='mySportsmans'), # Список спортсменов принадлежащих тренеру
    path('events', allEvents, name='allEvents'), # Список всех мероприятий
    path('EventSettings/<int:pk>/', EventSettings, name='EventSettings'), # Добавление соревнований в мероприятии
    path('SportsmanAdd/<int:pk>/', SportsmanAdd, name='SportsmanAdd'),# Добавить спортсмена на мероприятие
    path('Eventresults/<int:event>/', eventShow, name='eventShow'),  # Посмотреть список соревнований на мероприятии

    path('Eventresults/<int:event>/<int:sport>/', resultEvent, name='resultEvent'), #Добавление результата к пользователю на соревнованиях


    path('', myEvent, name='event'),
    path('calculator/', calculator, name='calculator'),


]