from django.db import models
from trip_management_app.models import Vehicle

# Create your models here.
class GpsData(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField()
    time = models.DateTimeField()