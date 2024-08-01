
from rest_framework.response import Response
from rest_framework.decorators import api_view
from auth_app.models import VendorProfile, AdminProfile
from .models import Route
from bill_report_app.models import Contract
from django.shortcuts import get_object_or_404
from .serializers import ContractSerializer

@api_view(['PUT'])
def assign_route(request):
    route_id = request.data.get('route_id')
    vendor_id = request.data.get('vendor_id')
    
    route = get_object_or_404(Route, id=route_id)
    vendor = get_object_or_404(VendorProfile, id=vendor_id)
    
    # Assuming there is a many-to-many or a related field for assignment
    # For demonstration, let's say we add a ManyToManyField in the Route model:
    # route.vendors.add(vendor)
    
    return Response({'status': 'Route assigned successfully'})

@api_view(['PUT'])
def assign_contract(request):
    contract_id = request.data.get('contract_id')
    vendor_id = request.data.get('vendor_id')
    admin_id = request.data.get('admin_id')
    
    contract = get_object_or_404(Contract, id=contract_id)
    vendor = get_object_or_404(VendorProfile, id=vendor_id)
    admin = get_object_or_404(AdminProfile, id=admin_id)
    
    # Assign contract to vendor and associate with admin
    contract.vendor = vendor
    contract.admin = admin
    contract.save()
    serializer=ContractSerializer(contract)
    Response(serializer.data)
    
    
    return Response({'status': 'Contract assigned successfully'})
