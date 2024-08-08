from rest_framework import permissions
class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'employee'