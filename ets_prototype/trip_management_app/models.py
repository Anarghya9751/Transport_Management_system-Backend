from django.db import models
from auth_app.models import DriverProfile, EmployeeProfile, CustomUser, VendorProfile

from utils.useful_functions import generate_id

# Create your models here.

def generate_vehicle_id():
    return "GA" + generate_id()

def generate_route_id():
    return "RO" + generate_id()

def generate_trip_id():
    return "TR" + generate_id()

class Vehicle(models.Model):
    Vehicle_id = models.CharField(max_length=20, default=generate_vehicle_id)
    vehicle_type = models.CharField(max_length=20, choices=(("car", "Car"), ("van", "Van"), ("bus", "Bus"), ("other", "Other")))
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, default="active", choices=(("active", "Active"), ("busy", "Busy"), ("inactive", "Inactive")))
    last_maintenance_date = models.DateField()
    
    def __str__(self):
        return self.Vehicle_id
    
    
class Route(models.Model):
    route_id = models.CharField(max_length=20, default=generate_route_id)
    vendor_id = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, null=True, blank=True)
    source_latitude = models.FloatField()
    source_longitude = models.FloatField()
    destination_latitude = models.FloatField()
    destination_longitude = models.FloatField()
    distance = models.FloatField()
    duration = models.FloatField()
    status = models.CharField(max_length=20, default="active", choices=(("active", "Active"), ("busy", "Busy"), ("inactive", "Inactive")))
    
    
    def __str__(self):
        return self.route_id
    
    
class Trip(models.Model):
    trip_id = models.CharField(max_length=20, default=generate_trip_id)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, default="pending", choices=(("pending", "Pending"), ("scheduled", "Scheduled"), ("completed", "Completed"), ("cancelled", "Cancelled")))
    start_latitude = models.FloatField(null=True, blank=True)
    start_longitude = models.FloatField(null=True, blank=True)
    end_latitude = models.FloatField(null=True, blank=True)
    end_longitude = models.FloatField(null=True, blank=True)
    

    
    def __str__(self):
        return self.trip_id
    

# Employee transport request will be added from here
class TransportRequest(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateTimeField()
    type = models.CharField(max_length=20, choices=(("pickup", "Pickup"), ("dropoff", "Dropoff")))
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed')
    ])
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.status} on {self.request_date}"
    

# Other Trip types like Escort, Multiple Day Trip, On Demand Trip will be added from here
class OtherRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=(("escort", "Escort"), ("multiple_day_trip", "Multiple Day Trip"), ("on_demand", "On Demand")))
    guest_name = models.TextField()
    guest_contact_number = models.IntegerField()
    request_date = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField()
    source_latitude = models.FloatField()
    source_longitude = models.FloatField()
    destination_latitude = models.FloatField()
    destination_longitude = models.FloatField()
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, default="pending", choices=(("pending", "Pending"), ("scheduled", "Scheduled"), ("completed", "Completed"), ("cancelled", "Cancelled")))
    start_latitude = models.FloatField()
    start_longitude = models.FloatField()
    end_latitude = models.FloatField()
    end_longitude = models.FloatField()
    days = models.IntegerField()

    def __str__(self):
        return f"{self.guest_name} - {self.status} on {self.request_date}"