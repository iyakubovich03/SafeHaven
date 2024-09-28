from rest_framework import serializers
from .models import UserLocation, ShelterLocation, UnverifiedShelter


from rest_framework import serializers
from .models import UnverifiedShelter

class UnverifiedShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnverifiedShelter
        fields = '__all__'

    def validate(self, data):
        address = data.get('address')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        existing_shelter = UnverifiedShelter.objects.filter(
            address=address,
            latitude=latitude,
            longitude=longitude
        )

        if self.instance:
            existing_shelter = existing_shelter.exclude(pk=self.instance.pk)

        if existing_shelter.exists():
            raise serializers.ValidationError("A shelter with this address, latitude, and longitude already exists.")

        return data


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