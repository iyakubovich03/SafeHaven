
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserLocation, ShelterLocation
from .serializers import UserLocationSerializer, CoordinatesListSerializer
from . secrets import get_api_key

import requests
import json


def get_most_recent_location():
    try:
        location = UserLocation.objects.latest('timestamp')
        return location.latitude, location.longitude
    except UserLocation.DoesNotExist:
        return None, None
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

class FetchAndSaveSheltersView(APIView):
    def searchfunct(self):
        latitude,longitude = get_most_recent_location()

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
            "X-Goog-FieldMask": "places.displayName,places.location"
        }
        response = requests.post(url, headers=header, data=json.dumps(data))
        return response.json()

    def get(self,request):
        coordinates=[]
        response = self.searchfunct()

        for lipo in response.get('places',[]):
            name=lipo.get('displayName').get('text')
            latitude=lipo.get('location').get('latitude')
            longitude=lipo.get('location').get('longitude')

            if name is not None and latitude is not None and longitude is not None:
                ShelterLocation.objects.update_or_create(
                    name=name,
                    defaults={'latitude': latitude, 'longitude': longitude})
                coordinates+=[{'latitude': latitude, 'longitude': longitude}]
        serializer = CoordinatesListSerializer(data={"coordinates": coordinates})

        if serializer.is_valid():
            return Response(serializer.data)  # Return serialized data in the response (when accessing the api should return)
        else:
            return Response(serializer.errors, status=400)



