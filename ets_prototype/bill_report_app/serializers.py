from rest_framework import serializers
from .models import Bill
from auth_app.models import CustomUser,AdminProfile

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['company', 'vendor', 'driver', 'bill_date', 'amount']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']