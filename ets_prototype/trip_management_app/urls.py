from django.urls import path
from .views import get_driver_with_trips, get_assigned_trips
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('api/drivers/<int:driver_id>/', get_driver_with_trips, name='get_driver_with_trips'),
    path('api/drivers/<int:driver_id>/trips/', get_assigned_trips, name='get_assigned_trips'),
]