from django.urls import path
from .views import UpdateUserLocationView, FetchAndSaveSheltersView, UnverifiedShelterCreateView, UnverifiedShelterUpdateView

urlpatterns = [
    path('update-location/', UpdateUserLocationView.as_view(), name='update-location'),
    path('fetch-shelters/', FetchAndSaveSheltersView.as_view(), name='get-shelters-save'),
    path('unverified-shelters/', UnverifiedShelterCreateView.as_view(), name='unverified-shelter-create'),
    path('unverified-shelters/<int:id>/', UnverifiedShelterUpdateView.as_view(), name='unverified-shelter-update'),
]

