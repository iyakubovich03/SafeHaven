from django.urls import path
from .views import UpdateUserLocationView, FetchAndSaveSheltersView,fetchShelterResrouces, UnverifiedShelterCreateView, UnverifiedShelterUpdateView, UnverifiedShelterListView, UnverifiedShelterUpdateView

urlpatterns = [
    path('update-location/', UpdateUserLocationView.as_view(), name='update-location'),
    path('fetch-shelters/', FetchAndSaveSheltersView.as_view(), name='get-shelters-save'),
    path('unverified-shelters/', UnverifiedShelterCreateView.as_view(), name='unverified-shelter-create'),
    path('unverified-shelters/<int:id>/', UnverifiedShelterUpdateView.as_view(), name='unverified-shelter-update'),
    path('shelter-resources/',fetchShelterResrouces.as_view(), name='shelter-resources'),
    path('api/unverified-shelters/', UnverifiedShelterListView.as_view(), name='unverified-shelter-list'),
    path('unverified-shelters/<int:id>/', UnverifiedShelterUpdateView.as_view(), name='unverified-shelter-update'),
]

