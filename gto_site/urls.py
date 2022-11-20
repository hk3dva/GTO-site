from django.contrib import admin
from django.urls import path, include
from registrationUser import views
from eventHandler import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('registrationUser.urls')),
    path('', include('eventHandler.urls')),
]
