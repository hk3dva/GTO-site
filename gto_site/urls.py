from django.contrib import admin
from django.urls import path, include
from registrationUser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registrationUser.urls')),
]
