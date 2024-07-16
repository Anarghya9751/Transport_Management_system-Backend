from django.db import models

# Create your models here.

def generate_vehicle_id():
    return "GA" + datetime.now().strftime("%Y%m%d%H%M%S") + ''.join(random.choice(string.ascii_uppercase) for _ in range(5))


class Vehicle(models.Model):
    Vehicle_id = models.CharField(max_length=20, default=generate_vehicle_id)
    vehicle_type = models.CharField(max_length=20, choices=(("car", "Car"), ("van", "Van"), ("bus", "Bus"), ))
    