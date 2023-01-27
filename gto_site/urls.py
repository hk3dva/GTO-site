from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from registrationUser import views
from eventHandler import views

urlpatterns = [
    path('', include('mainpage.urls')),
    path('admin/', admin.site.urls),
    path('register/', include('registrationUser.urls')),
    path('event/', include('eventHandler.urls')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)