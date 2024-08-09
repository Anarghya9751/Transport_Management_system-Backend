from django.urls import path
from .views import generate_bill_view

urlpatterns = [
    path('generate-bill/', generate_bill_view, name='generate-bill'),
]
