# spookle/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('events/', include('events.urls')),
    path('about/', views.about, name='about'),
    path('sightings/', include('sightings.urls')),
    path('contact/', views.contact, name='contact')
    ]
