
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserLocation
from .serializers import UserLocationSerializer
from . secrets import get_api_key
import requests
import json

class UpdateUserLocationView(APIView):
    def post(self, request, *args, **kwargs):



        # Extract latitude and longitude from the request
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        if not latitude or not longitude:
            return Response({"error": "Latitude and Longitude are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Update or create a new location record for the user
        location, created = UserLocation.objects.update_or_create(
            defaults={'latitude': latitude, 'longitude': longitude}
        )
        serializer = UserLocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def searchfunc(self,latitude,longitude):

        url="https://places.googleapis.com/v1/places:searchText"
        apikey=get_api_key()
        data={
          "textQuery": "emergency shelters",
          "locationBias": {
            "circle": {
              "center": {
                "latitude": latitude,
                "longitude": longitude
              },
              "radius": 500.0
            }
          }
        }

        header = {
            "Content-Type": 'application/json',
            "X-Goog-Api-Key": apikey,
            "X-Goog-FieldMask": "places.displayName,places.name,places.location"
        }
        response = requests.post(url, headers=header, data=json.dumps(data))
