from rest_framework import serializers
from .models import  Trip
from auth_app.models import DriverProfile,CustomUser



class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True, read_only=True)

    class Meta:
        model = DriverProfile
        fields = '__all__'
class CustomUserSearilizer(serializers.ModelSerializer):
    class Meta:
        fields=["username","email"]

class UserSerializer(serializers.ModelSerializer):
       class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

       
       
       


