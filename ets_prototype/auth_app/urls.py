
from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.vendor_list_create, name='vendor-list-create'),
    path('vendors/<int:pk>/', views.vendor_detail_update_delete, name='vendor-detail-update-delete'),
]
