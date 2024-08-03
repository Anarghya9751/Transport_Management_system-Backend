from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Bill, Trip, Vehicle, CompanyProfile, DriverProfile, Configuration
from django.http import HttpResponse
from .utils import generate_bill


def generate_bill_view(request):
    trip_id = request.GET.get('trip_id')
    vehicle_id = request.GET.get('vehicle_id')
    company_id = request.GET.get('company_id', None)  # company_id is optional
    driver_id = request.GET.get('driver_id')
    distance = float(request.GET.get('distance', 0))

    if not trip_id or not vehicle_id or not driver_id or not distance:
        return HttpResponse('Missing required parameters', status=400, content_type='text/plain')

    bill = generate_bill(trip_id, vehicle_id, company_id, driver_id, distance)

    response_text = f'''
    Bill generated successfully with ID: {bill.bill_id}
    Amount: {bill.amount}
    Bill Date: {bill.bill_date}
    Distance: {bill.distance}
    '''
    
    return HttpResponse(response_text, content_type='text/plain')


Configuration.objects.set_value('RATE_PER_KM', '15.0')
rate_per_km = float(Configuration.objects.get_value('RATE_PER_KM', '0.0'))



def get_rate_per_km(request):
    rate_per_km = float(Configuration.objects.get_value('RATE_PER_KM', '0.0'))
    return HttpResponse(f'Rate per km: {rate_per_km}', content_type="text/plain")


