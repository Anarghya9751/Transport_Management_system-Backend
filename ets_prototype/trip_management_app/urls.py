# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('start-trip/', views.start_trip, name='start_trip'),
    path('end-trip/', views.end_trip, name='end_trip'),
]
