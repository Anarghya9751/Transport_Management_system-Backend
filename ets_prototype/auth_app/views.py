from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from auth_app.models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from .permissions import IsEmployee,IsDriver,IsAdmin,IsVendor,IsCompany,IsCommander


@api_view(['POST'])
@permission_classes([AllowAny])
class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsEmployee])
def employee_transport_request(request):
    if request.method == 'GET':
        return Response({"message": "GET transport request"}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response({"message": "POST transport request"}, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsEmployee])
def call_driver(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET driver request"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST driver request"}, status=200)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsEmployee])
def sos_panic_button(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET SOS/panic request"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST SOS/panic request"}, status=200)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsEmployee])
def get_transport_status(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET transport status"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST transport status"}, status=201)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,IsDriver])
def driver_assigned_trips_detail(request):
    if request.method == 'GET':
        return Response({"message": "GET assigned trip "}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        return Response({"message": "POST assigned trip "}, status=status.HTTP_201_CREATED)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,IsDriver])
def call_employee(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET driver request"}, status=200)
    elif request.method == 'POST':
         return JsonResponse({"message": "POST driver request"}, status=200)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,IsDriver])
def start_trip(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET start trip"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST start trip"}, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsDriver])
def end_trip(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET end trip"}, status=200)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def admin_live_tracking_vehicles(request):
    return Response({"message": "Admin live tracking vehicles"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def admin_live_tracking_employees(request):
    return Response({"message": "Admin live tracking employees"}, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def management_of_routes_schedules_allocations(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET management of routes, schedules, and allocations"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST management of routes, schedules, and allocations"}, status=201)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def vendor_allocation(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET vendor allocation"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST vendor allocation"}, status=201)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def Assignment_of_routes_and_contracts_to_vendor(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET assignment of routes and contracts to vendor"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST assignment of routes and contracts to vendor"}, status=201)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def vendor_performance(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET vendor performance"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST vendor performance"}, status=201)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def admin_get_bills(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET get_admin bills"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST get_admin bills"}, status=201)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def admin_generate_reports(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET generate_admin reports"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST generate_admin reports"}, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsVendor])
def vendor_live_tracking_vehicles(request):
    return Response({"message": "Vendor live tracking vehicles"}, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsVendor])
def vendor_get_bills(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET vendor_get bills"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST vendor_get bills"}, status=201)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsVendor])
def vendor_generate_reports(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET generate_vendor reports"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST generate_vendor reports"}, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsCompany])
def company_live_tracking_employees(request):
    return Response({"message": "company live tracking employees"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsCompany])
def company_live_tracking_vehicles(request):
    return Response({"message": "Company live tracking vehicles"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsCompany])
def Company_get_bills(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET company_get bills"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST company_get bills"}, status=201)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsCompany])
def Company_generate_reports(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET generate_company reports"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"message": "POST generate_company reports"}, status=201)


