from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #Employee permissions

    path('api/employee/transport-request/', employee_transport_request, name='transport-request'),
    path('api/employee/call-driver/', call_driver, name='call-driver'),
    path('api/employee/sos-panic-button/', sos_panic_button, name='sos-panic-button'),
    path('api/employee/get-transport-status/', get_transport_status, name='get-transport-status'),

    #Driver Permissions

    path('api/driver/assigned-trips/', driver_assigned_trips_detail, name='assigned-trips'),
    path('api/driver/call-employee/', call_employee, name='call-employee'),
    path('api/driver/start-trip/', start_trip, name='start-trip'),
    path('api/driver/end-trip/', end_trip, name='end-trip'),

    # Admin permissions
    path('api/admin/live-tracking-vehicles/', admin_live_tracking_vehicles, name='admin-live-tracking-vehicles'),
    path('api/admin/live-tracking-employees/', admin_live_tracking_employees, name='admin-live-tracking-employees'),
    path('api/admin/management-of-routes-schedules-allocations/', management_of_routes_schedules_allocations, name='admin-management-of-routes-schedules-allocations'),
    path('api/admin/Vendor-allocation/', vendor_allocation, name='admin-vendor-allocation'),
    path('api/admin/Assignment-of-routes-and-contracts-to-vendor/', Assignment_of_routes_and_contracts_to_vendor, name='Assignment-of-routes-and-contracts-to-vendor'),
    path('api/admin/vendor-performance/', vendor_performance, name='admin-vendor-performance'),
    path('api/admin/get-bills/', admin_get_bills, name='admin-get-bills'),
    path('api/admin/generate-reports/', admin_generate_reports, name='admin-generate-reports'),

    #vendor permissions
    path('api/vendor/live-tracking-vehicles/', vendor_live_tracking_vehicles, name='vendor-live-tracking-vehicles'),
    path('api/vendor/get-bills/', vendor_get_bills, name='vendor-get-bills'),
    path('api/vendor/generate-reports/', vendor_generate_reports, name='vendor-generate-reports'),

    #company permissions
    path('api/company/live-tracking-vehicles/', company_live_tracking_vehicles, name='company-live-tracking-vehicles'),
    path('api/company/live-tracking-employees/', company_live_tracking_employees, name='company-live-tracking-employees'),
    path('api/company/get-bills/', Company_get_bills, name='company-get-bills'),
    path('api/company/generate-reports/', Company_generate_reports, name='company-generate-reports'),
    
]
