from rest_framework import permissions

class RestrictEditPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and (obj.is_public or obj.owner == request.user):
            return True
        else:
            '''Trying to edit, must be the owner'''
            return obj.owner == request.user