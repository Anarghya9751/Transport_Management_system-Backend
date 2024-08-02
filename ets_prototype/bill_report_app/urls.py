from django.urls import path
from . import views

urlpatterns = [
    path('generate_pdf/', views.my_view, name='generate_pdf'),
]
