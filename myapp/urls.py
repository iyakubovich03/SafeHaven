from django.urls import path
from .views import UpdateUserLocationView

urlpatterns = [
    path('update-location/', UpdateUserLocationView.as_view(), name='update-location'),
]