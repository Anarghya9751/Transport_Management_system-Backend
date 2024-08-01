from django.urls import path
from .views import get_driver_with_trips, get_assigned_trips

urlpatterns = [
    path('api/drivers/<int:driver_id>/', get_driver_with_trips, name='get_driver_with_trips'),
    path('api/drivers/<int:driver_id>/trips/', get_assigned_trips, name='get_assigned_trips'),
]
