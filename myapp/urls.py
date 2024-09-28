from django.urls import path
from .views import UpdateUserLocationView, FetchAndSaveSheltersView,fetchShelterResrouces

urlpatterns = [
    path('update-location/', UpdateUserLocationView.as_view(), name='update-location'),
    path('fetch-shelters/', FetchAndSaveSheltersView.as_view(), name='get-shelters-save'),
    path('shelter-resources/',fetchShelterResrouces.as_view(), name='shelter-resources'),
]