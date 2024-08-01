
from django.urls import path
from .views import assign_route, assign_contract

urlpatterns = [
    path('assign_route/', assign_route, name='assign_route'),
    path('assign_contract/', assign_contract, name='assign_contract'),
]
