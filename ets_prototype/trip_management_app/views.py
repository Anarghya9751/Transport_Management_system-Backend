from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from auth_app.models import EmployeeProfile
from trip_management_app.models import TransportRequest
from .serializers import EmployeeSerializer, TransportRequestSerializer

@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = EmployeeProfile.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def transport_request_list(request):
    if request.method == 'GET':
        transport_requests = TransportRequest.objects.all()
        serializer = TransportRequestSerializer(transport_requests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TransportRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    try:
        employee = EmployeeProfile.objects.get(pk=pk)
    except EmployeeProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def transport_request_detail(request, pk):
    try:
        transport_request = TransportRequest.objects.get(pk=pk)
    except TransportRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransportRequestSerializer(transport_request)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TransportRequestSerializer(transport_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        transport_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
