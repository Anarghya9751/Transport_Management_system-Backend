from django.urls import path
from trip_management_app.views import *

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:pk>/', employee_detail, name='employee_detail'),
    path('transport-requests/', transport_request_list, name='transport_request_list'),
    path('transport-requests/<int:pk>/', transport_request_detail, name='transport_request_detail'),
]
