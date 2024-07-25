from rest_framework import serializers
from auth_app.models import CustomUser, EmployeeProfile, DriverProfile, AdminProfile,VendorProfile,CompanyProfile

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']
