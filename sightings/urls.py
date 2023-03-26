from django.urls import path
from .views import sightings, sighting_detail

urlpatterns = [
    path('sightings/', sightings, name='sightings'),
    path('sighting/<int:sighting_id>/', sighting_detail, name='sighting_detail'),
]