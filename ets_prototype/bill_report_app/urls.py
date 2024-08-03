from django.urls import path
from .views import generate_bill_view, get_rate_per_km

urlpatterns = [
    path('generate-bill/', generate_bill_view, name='generate-bill'),
    path('get-rate-per-km/', get_rate_per_km, name='get-rate-per-km'),
]
