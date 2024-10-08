from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    path('', views.handle_index),
    path('contacts/', views.handle_contacts),
    path('about/', views.handle_about),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)