# import from stl 
from rest_framework.permissions import BasePermission , SAFE_METHODS
## SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
# import from 
from api.models import drf_courses
class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_permission(self, request, view , *args , **kwargs):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff 
        )

class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return bool (
            # get access to superuser or author of object
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.author == request.user
        )

class IsSuperuserOrOwnerReadOnly(BasePermission):
    """
    Object-level permission to only allow superuser or owner of an object to read it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # get acces to author to readonly 
        if request.method in SAFE_METHODS and request.user.is_authenticated and request.user.is_staff:
            return True

        # Instance must have an attribute named `owner`.
        return bool (
            # get access to superuser full
            request.user.is_superuser
        )