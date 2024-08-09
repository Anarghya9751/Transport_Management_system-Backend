from django.contrib import admin

from .models import Alerts, SafetyLogs

# Register your models here.
admin.site.register(Alerts)
admin.site.register(SafetyLogs)