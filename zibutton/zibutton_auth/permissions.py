from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    '''
    Only allow authenticated users to view and edit their OWN user data.
    '''

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user