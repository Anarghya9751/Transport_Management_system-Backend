# vendors/serializers.py

from rest_framework import serializers
from .models import VendorProfile
from auth_app.models import CustomUser,AdminProfile

class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']
        
