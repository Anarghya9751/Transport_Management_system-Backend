from django.contrib import admin
from auth_app.models import EmployeeProfile
from auth_app.models import CustomUser
from trip_management_app.models import TransportRequest

# Register your models here.
admin.site.register(EmployeeProfile)
admin.site.register(CustomUser)
admin.site.register(TransportRequest)

