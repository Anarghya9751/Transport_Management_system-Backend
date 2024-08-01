# urls.py

from django.urls import path
from .views import TripReportView

urlpatterns = [
    path('trip-reports/', TripReportView.as_view(), name='trip-reports'),
]
