
from django.db import models
from django.contrib.auth.models import User


class UnverifiedShelter(models.Model):
    unique_identifier = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    total_capacity = models.IntegerField()
    available_beds = models.IntegerField()
    available_food = models.BooleanField(default=False)
    available_medical_supplies = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class UserLocation(models.Model):
   latitude = models.FloatField()
   longitude = models.FloatField()
   timestamp = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f"({self.timestamp}. -  {self.latitude}, {self.longitude})"
class ShelterLocation(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.name}. -  {self.latitude}, {self.longitude})"


