# serializers.py
from rest_framework import serializers
from .models import Trip
from auth_app.models import CustomUser,DriverProfile

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']