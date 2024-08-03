from django.contrib import admin
from .models import Bill, Contract
from .models import Configuration

# Register your models here.
admin.site.register(Bill)
admin.site.register(Contract)


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
