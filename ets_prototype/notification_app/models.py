from django.db import models

from auth_app.models import DriverProfile, EmployeeProfile
from trip_management_app.models import Vehicle, Trip
from utils.useful_functions import generate_id


def generate_alert_id():
    return "AL" + generate_id()

def generate_safety_log_id():
    return "SL" + generate_id()


# Create your models here.
class Alerts(models.Model):
    alert_id = models.CharField(max_length=20, default=generate_alert_id)
    alert_type = models.CharField(
        max_length=20,
        choices=(
            ("live", "Live"),
            ("sos", "SOS"),
            ("network", "Network"),
            ("location", "Location"),
            ("speed", "Speed"),
            ("delay", "Delay"),
            ("idle", "Idle"),
        ),
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    alert_status = models.CharField(choices=(("active", "Active"), ("inactive", "Inactive")), max_length=20)
    driver_id = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.alert_id
    

class SafetyLogs(models.Model):
    safety_log_id = models.CharField(max_length=20, default=generate_safety_log_id)
    alert_id = models.ForeignKey(Alerts, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.alert_id
