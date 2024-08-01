from django.contrib import admin

from .models import Vehicle, Route, Trip, TransportRequest, OtherRequest

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(TransportRequest)
admin.site.register(OtherRequest)


