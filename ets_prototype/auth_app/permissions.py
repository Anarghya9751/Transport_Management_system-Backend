from rest_framework.permissions import BasePermission

class IsAdminOrVendorOrCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (
            request.user.role in ['admin', 'vendor', 'company']
        )

class IsAdminOrCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (
            request.user.role in ['admin', 'company']
        )

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (
            request.user.role == 'admin'
        )

class IsDriver(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (
            request.user.role == 'driver'
        )
class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (
            request.user.role == 'employee'
        )