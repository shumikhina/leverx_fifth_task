from rest_framework.permissions import BasePermission

from authapp.models import User


class StudentAllowed(BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.role == User.STUDENT
