from django.urls import path
from . import views

urlpatterns = [
    path('trips/', views.trip_list),
    path('trips/<int:pk>/', views.trip_detail),
]
