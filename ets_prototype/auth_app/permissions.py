from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'

class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'employee'

class IsDriver(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Driver'

class IsVendor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'vendor'

class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'company'
    
class IsCommander(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Commander'




