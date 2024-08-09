from .models import Bill, Trip, Vehicle, CompanyProfile, DriverProfile, Configuration
from django.utils import timezone
from django.shortcuts import get_object_or_404

def generate_bill(trip_id, vehicle_id, company_id, driver_id, distance):
    trip = get_object_or_404(Trip, id=trip_id)
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    company = get_object_or_404(CompanyProfile, id=company_id)
    driver = get_object_or_404(DriverProfile, id=driver_id)
    rate_per_km = float(Configuration.objects.get_value('RATE_PER_KM', '0.0'))
    amount = distance * rate_per_km

    # Create and save the new bill
    new_bill = Bill(
        trip_id=trip,
        vehicle_id=vehicle,
        company_id=company,
        driver_id=driver,
        amount=amount,
        bill_date=timezone.now(),
        distance=distance
    )
    new_bill.save()

    return new_bill
