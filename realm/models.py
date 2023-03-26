from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    dob = models.DateField(null=True)
    country = models.CharField(max_length=255)
    attending = models.ManyToManyField(
        Event, blank=True, related_name="attending")


