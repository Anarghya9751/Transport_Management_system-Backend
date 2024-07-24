from rest_framework import serializers
from auth_app.models import EmployeeProfile
from trip_management_app.models import TransportRequest

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = "__all__"

class TransportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportRequest
        fields = "__all__"