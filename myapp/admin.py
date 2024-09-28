from django.contrib import admin
from django.contrib import admin
from .models import UserLocation, ShelterLocation, ShelterResources

admin.site.register(UserLocation)
admin.site.register(ShelterLocation)
admin.site.register(ShelterResources)
# Register your models here.
