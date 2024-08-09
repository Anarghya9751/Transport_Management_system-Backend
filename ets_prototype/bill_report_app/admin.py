from django.contrib import admin

from .models import Bill, Contract

# Register your models here.
admin.site.register(Bill)
admin.site.register(Contract)