from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthenticatedAndIsActive(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_active
        )
