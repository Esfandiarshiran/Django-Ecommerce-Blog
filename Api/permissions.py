from rest_framework import permissions
from django.contrib.auth.models import User

# Customize permission written by Esfandiar Shiran. All user can see
# and also use Api, but just admin and (Post author) are allowed to add or edite(POST and PUT) Product and Post.
# Note that in the setting we determined just user who were login can use Api not guests,
# moreover we need to limited user to access (POST, PUT, and DELETE) even if ordinary.


class IsadminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        return False
