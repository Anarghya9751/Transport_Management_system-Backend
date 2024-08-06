from rest_framework import permissions
class IsDriver(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'driver'

