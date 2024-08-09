from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import VendorProfile
from .serializers import VendorProfileSerializer

@api_view(['GET', 'POST'])
def vendor_list_create(request):
    """
    List all vendors or create a new vendor profile.
    """
    if request.method == 'GET':
        vendors = VendorProfile.objects.all()
        serializer = VendorProfileSerializer(vendors, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = VendorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assumes the user is authenticated
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail_update_delete(request, pk):
    """
    Retrieve, update, or delete a vendor profile.
    """
    vendor = get_object_or_404(VendorProfile, pk=pk)

    if request.method == 'GET':
        serializer = VendorProfileSerializer(vendor)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = VendorProfileSerializer(vendor, data=request.data, partial=True)  # Allow partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
