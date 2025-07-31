from rest_framework import permissions

class RestrictCreatePermission(permissions.BasePermission):
    '''
    Custom permission to only allow authenticated users to create objects.
    '''
    
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        else:
            return True

class RestrictEditPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and (obj.is_public or obj.owner == request.user):
            return True
        else:
            '''Trying to edit, must be the owner'''
            return obj.owner == request.user