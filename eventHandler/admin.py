from django.contrib import admin
from .models import *

admin.site.register(SportObject)

admin.site.register(Team)

admin.site.register(Event)

admin.site.register(SportTypeEvent)

admin.site.register(SportTypeEventHasEvent)

admin.site.register(SportType)

admin.site.register(SportsmanSportTypeEvent)

