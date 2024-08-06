from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bill
from .serializers import BillSerializer
from django.db.models import Sum, Count
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from auth_app.models import CustomUser
from .permissions import IsAdmin
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
#@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdmin])
class TripReportView(APIView):
    def get(self, request, *args, **kwargs):
        from_date = request.query_params.get('from')
        to_date = request.query_params.get('to')
        report_type = request.query_params.get('report_type')
        report_type_company = request.query_params.get('report_type_company')
        report_type_value = request.query_params.get('report_type_value')
        access_level = request.query_params.get('access_level')

        if not from_date or not to_date:
            return Response({'error': 'Please provide both from and to dates.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            to_date = datetime.strptime(to_date, '%Y-%m-%d')
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
        
        filters = {'bill_date__range': (from_date, to_date)}
        if report_type:
            filters['report_type'] = report_type
        if report_type_company:
            filters['report_type_company'] = report_type_company
        if report_type_value:
            filters['report_type_value'] = report_type_value
        if access_level:
            filters['access_level'] = access_level
        
        bills = Bill.objects.filter(**filters)
        total_amount = bills.aggregate(Sum('amount'))['amount__sum'] or 0.0
        total_trips = bills.aggregate(Count('id'))['id__count']
        
        serializer = BillSerializer(bills, many=True)
        report_data = {
            'total_amount': total_amount,
            'total_trips': total_trips,
            'bills': serializer.data
        }
        return Response(report_data, status=status.HTTP_200_OK)