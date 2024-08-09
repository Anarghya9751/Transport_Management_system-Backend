from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Bill, Trip, Vehicle, CompanyProfile, DriverProfile, Configuration
from .utils import generate_bill
from .serializers import BillSerializer

def generate_bill(trip):
    
    # Create and save the new bill
    new_bill = Bill(
        trip=trip,
        vehicle=trip.vehicle,
        company=trip.company,
        driver=trip.driver,
        amount=trip.route.distance * float(Configuration.objects.get_value('rate_per_km', default='0.0')),
        bill_date=timezone.now(),
        distance=trip.route.distance
    )
    new_bill.save()

    return new_bill

@api_view(['POST'])
def generate_bill_view(request):
    trip = get_object_or_404(Trip, id=request.data['trip_id'])
    bill = generate_bill(trip)
    serializer = BillSerializer(bill)
    return Response(serializer.data)