from rest_framework import serializers
from .models import UserLocation, ShelterLocation,ShelterResources


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ['latitude', 'longitude', 'timestamp']

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelterLocation
        fields = ['name', 'latitude', 'longitude','place']


class CoordinateSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

# Define the serializer for the list of tuples
class CoordinatesListSerializer(serializers.Serializer):
    coordinates = serializers.ListField(
        child=CoordinateSerializer()  # essentialy holds the object in dctionary kind of setting
    )
class ShelterResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelterResources
        fields = ['name','food','beds','water','electricity', 'first_aid']