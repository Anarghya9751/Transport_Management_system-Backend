from django.db import models
from auth_app.models import DriverProfile, EmployeeProfile

from utils.useful_functions import generate_id

# Create your models here.

def generate_vehicle_id():
    return "GA" + generate_id()

def generate_vehicle_id():
    return "RO" + generate_id()


class Vehicle(models.Model):
    Vehicle_id = models.CharField(max_length=20, default=generate_vehicle_id)
    vehicle_type = models.CharField(max_length=20, choices=(("car", "Car"), ("van", "Van"), ("bus", "Bus"), ("other", "Other")))
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, default="active", choices=(("active", "Active"), ("busy", "Busy"), ("inactive", "Inactive")))
    last_maintenance_date = models.DateField()
    
    def __str__(self):
        return self.Vehicle_id
    
    
class Route(models.Model):
    route_id = models.CharField(max_length=20, default=generate_vehicle_id)
    origin_latitude = models.FloatField()
    origin_longitude = models.FloatField()
    destination_latitude = models.FloatField()
    destination_longitude = models.FloatField()
    distance = models.FloatField()
    duration = models.FloatField()
    status = models.CharField(max_length=20, default="active", choices=(("active", "Active"), ("busy", "Busy"), ("inactive", "Inactive")))
    
    
    def __str__(self):
        return self.route_id
    
    
class Trip(models.Model):
    trip_id = models.CharField(max_length=20, default=generate_vehicle_id)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, default="pending", choices=(("pending", "Pending"), ("scheduled", "Scheduled"), ("completed", "Completed"), ("cancelled", "Cancelled")))

    
    def __str__(self):
        return self.trip_id
    

class TransportRequest(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    # vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateTimeField()
    type = models.CharField(max_length=20, choices=(("pickup", "Pickup"), ("dropoff", "Dropoff")))
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed')
    ])

    def __str__(self):
        return f"{self.employee} - {self.status} on {self.request_date}"

    
    
# from django.db import models

# # Create your models here.
# class vehicle(models.Model):
#     vehicle_id= models.IntegerField(primary_key=True)
#     license_plate=models.CharField(max_length=30)
#     type=models.CharField(max_length=40)
#     current_location=models.CharField(max_length=50)

# class trip(models.Model):
#     trip_id=models.IntegerField(primary_key=True)
#     user_id=models.IntegerField()
#     vehicle_id=models.IntegerField()
#     status=models.CharField(max_length=40)
#     start_tim=models.DateTimeField()
#     end_time=models.DateTimeField()

# class route(models.Model):
#     trip_id=models.IntegerField(primary_key=True)
#     route_pin=models.IntegerField()

# class transportrequest(models.Model):
#     emp_id=models.IntegerField(primary_key=True)
#     date=models.DateField()
#     pick_up=models.CharField(max_length=40)
#     droup=models.CharField(max_length=40)