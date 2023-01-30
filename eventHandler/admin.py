from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(City)
admin.site.register(SportObject)
admin.site.register(Organization)


admin.site.register(Event)

admin.site.register(SportTypeEvent)
admin.site.register(SportTypeEventHasEvent)
admin.site.register(SportsmanSportTypeEvent)
admin.site.register(Sport_type_in_sport_object)


admin.site.register(SportType)
admin.site.register(Standards)




