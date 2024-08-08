
from django.urls import path
from .views import assign_route, assign_contract
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('assign_route/', assign_route, name='assign_route'),
    path('assign_contract/', assign_contract, name='assign_contract'),
]
