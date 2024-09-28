
from django.db import models
from django.contrib.auth.models import User


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




