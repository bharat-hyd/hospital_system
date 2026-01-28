from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "ADMIN"

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "DOCTOR"
