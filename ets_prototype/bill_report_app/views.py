from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Sum, Count
from datetime import datetime, timedelta
from .models import Bill
from .serializers import BillSerializer
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

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdmin])
def generate_report(request):
    payload = request.data

    # Extract filter parameters
    start_date = payload.get('start_date')
    end_date = payload.get('end_date')
    company = payload.get('company')
    vendor = payload.get('vendor')
    driver = payload.get('driver')
    report_type = payload.get('report_type')

    filters = {
        'bill_date__range': [start_date, end_date]
    }
    
    if company:
        filters['company'] = company
    if vendor:
        filters['vendor'] = vendor
    if driver:
        filters['driver'] = driver

    # Query for data
    bills = Bill.objects.filter(**filters)

    # Prepare response based on report_type
    if report_type == 'weekly':
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        report_data = []
        while start_date <= end_date:
            week_start = start_date - timedelta(days=start_date.weekday())
            week_end = week_start + timedelta(days=6)
            weekly_bills = bills.filter(bill_date__range=[week_start, week_end])
            total_amount = weekly_bills.aggregate(Sum('amount'))['amount__sum'] or 0
            total_trips = weekly_bills.count()
            report_data.append({
                'week_start': week_start,
                'week_end': week_end,
                'total_amount': total_amount,
                'total_trips': total_trips
            })
            start_date = week_end + timedelta(days=1)
        return Response(report_data)

    elif report_type == 'monthly':
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        report_data = []
        while start_date <= end_date:
            month_start = start_date.replace(day=1)
            month_end = (month_start + timedelta(days=31)).replace(day=1) - timedelta(days=1)
            monthly_bills = bills.filter(bill_date__range=[month_start, month_end])
            total_amount = monthly_bills.aggregate(Sum('amount'))['amount__sum'] or 0
            total_trips = monthly_bills.count()
            report_data.append({
                'month_start': month_start,
                'month_end': month_end,
                'total_amount': total_amount,
                'total_trips': total_trips
            })
            start_date = month_end + timedelta(days=1)
        return Response(report_data)

    elif report_type == 'yearly':
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        report_data = []
        while start_date <= end_date:
            year_start = start_date.replace(month=1, day=1)
            year_end = start_date.replace(month=12, day=31)
            yearly_bills = bills.filter(bill_date__range=[year_start, year_end])
            total_amount = yearly_bills.aggregate(Sum('amount'))['amount__sum'] or 0
            total_trips = yearly_bills.count()
            report_data.append({
                'year_start': year_start,
                'year_end': year_end,
                'total_amount': total_amount,
                'total_trips': total_trips
            })
            start_date = year_end + timedelta(days=1)
        return Response(report_data)

    return Response({'error': 'Invalid report_type'}, status=400)

