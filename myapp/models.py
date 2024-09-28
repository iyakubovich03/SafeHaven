
from django.db import models
from django.contrib.auth.models import User


class UserLocation(models.Model):
   latitude = models.FloatField()
   longitude = models.FloatField()
   timestamp = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f"({self.latitude}, {self.longitude})"
