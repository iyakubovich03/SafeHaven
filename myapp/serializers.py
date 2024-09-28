from rest_framework import serializers
from .models import UserLocation, ShelterLocation, UnverifiedShelter


class UnverifiedShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnverifiedShelter
        fields = '__all__'


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ['latitude', 'longitude', 'timestamp']
class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelterLocation
        fields = ['name', 'latitude', 'longitude']

class CoordinateSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

# Define the serializer for the list of tuples
class CoordinatesListSerializer(serializers.Serializer):
    coordinates = serializers.ListField(
        child=CoordinateSerializer()  # essentialy holds the object in dctionary kind of setting
    )