from django.contrib import admin
from django.urls import path, include

from registrationUser import views
from eventHandler import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('registrationUser.urls')),
    path('event/', include('eventHandler.urls')),
]
