from django.contrib import admin

from .models import CustomUser, AdminProfile, CommanderProfile, VendorProfile, CompanyProfile, DriverProfile, EmployeeProfile

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AdminProfile)
admin.site.register(CommanderProfile)
admin.site.register(VendorProfile)
admin.site.register(CompanyProfile)
admin.site.register(DriverProfile)
admin.site.register(EmployeeProfile)