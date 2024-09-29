
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class UnverifiedShelter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    total_capacity = models.IntegerField()
    available_beds = models.IntegerField()
    available_food = models.BooleanField()
    available_medical_supplies = models.BooleanField()
    electricity = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['address', 'latitude', 'longitude']

    def clean(self):
        existing_shelter = UnverifiedShelter.objects.filter(
            address=self.address,
            latitude=self.latitude,
            longitude=self.longitude
        ).exclude(pk=self.pk).first()

        if existing_shelter:
            raise ValidationError("A shelter with this address, latitude, and longitude already exists.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
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
    place=models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"({self.name}. -  {self.latitude}, {self.longitude} {self.place}"
    
class ShelterResources(models.Model):
    name = models.CharField(max_length=255, unique=True)
    food=models.IntegerField()
    beds = models.IntegerField()
    water=models.IntegerField()
    electricity = models.IntegerField()
    first_aid = models.IntegerField()

    def __str__(self):
        return f"Resources for {self.name}: beds available: {self.beds}, food available: {self.food}, medical supplies available: {self.first_aid}, electricity: {self.electricity}, water: {self.water}"




