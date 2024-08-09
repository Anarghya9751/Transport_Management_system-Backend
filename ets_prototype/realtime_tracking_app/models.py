from django.db import models
from trip_management_app.models import Vehicle

# Create your models here.
class GpsData(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.vehicle_id} - {self.time}"
    
    

{
    bills: [
        {
            "bill_no": 1,
            "amt": 4567,
            
        },
        {
            "bill_no": 1,
            "amt": 4567,
            
        }
    ]
}

report-type-value  # report type
"2024-2025" # yearly
"2022" # monthly
"jan-apr" # weekly

