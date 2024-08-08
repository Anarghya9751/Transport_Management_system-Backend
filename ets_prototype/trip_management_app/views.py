from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from auth_app.models import DriverProfile,CustomUser
from .models import Trip
from django.contrib.auth.models import User
from .serializers import DriverSerializer,TripSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsDriver

@api_view(['POSTS'])
@permission_classes([IsDriver])
class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsDriver]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsDriver])
def get_driver_with_trips(request, driver_id):
    try:
        driver = DriverProfile.objects.get(id=driver_id)
    except DriverProfile.DoesNotExist:
        return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = DriverSerializer(driver)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsDriver])
def get_assigned_trips(request, driver_id):
    try:
        driver = DriverProfile.objects.get(id=driver_id)
    except DriverProfile.DoesNotExist:
        return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

    # Retrieve trips assigned to the driver
    trips = Trip.objects.filter(driver_id=driver)
    serializer = TripSerializer(trips, many=True)

    response_data = {
        'name': driver.user.get_full_name(),
        'email': driver.user.email,
        'trips': serializer.data,
    }

    return Response(response_data, status=status.HTTP_200_OK)

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

