# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer
from django.utils import timezone

@api_view(['POST'])
def start_trip(request):
    trip_id = request.data.get('trip_id')
    pin = request.data.get('pin')
    meter_img = request.FILES.get('meter_img')
    if not trip_id or not pin:
        return Response({"error": "Trip ID and PIN are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        trip = Trip.objects.get(trip_id=trip_id)
        print(f"Stored PIN: {trip.pin}, Provided PIN: {pin}")
        print(type(trip.pin), type(pin))
        if str(trip.pin) != pin:
            return Response({"error": "Invalid PIN"}, status=status.HTTP_400_BAD_REQUEST)
        
        trip.start_time = timezone.now()
        trip.pin = pin
        trip.start_meter_img = meter_img
        trip.status = 'scheduled'
        trip.save()
        serializer = TripSerializer(trip)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Trip.DoesNotExist:
        return Response({"error": "Trip not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def end_trip(request):
    trip_id = request.data.get('trip_id')
    meter_img = request.FILES.get('meter_img')

    try:
        trip = Trip.objects.get(trip_id=trip_id)
        trip.end_time = timezone.now()
        trip.end_meter_img = meter_img
        trip.status = 'completed'
        trip.save()
        serializer = TripSerializer(trip)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Trip.DoesNotExist:
        return Response({"error": "Trip not found"}, status=status.HTTP_404_NOT_FOUND)
