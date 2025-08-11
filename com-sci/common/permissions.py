from rest_framework import permissions  

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        # Allow full access to only verified users.
        if request.user.is_verified:
            return True 
        return False 
    
    def has_object_permission(self, request, view, obj):
        # Allow Read-Only access to all users
        if request.method in permissions.SAFE_METHODS:
            return True 
        
        # Allow full access to admin users.
        if request.user.is_staff:
            return True 
        
        # Check if the object has a 'owner' attribute, then return the truthiness.
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        
        # Check if the object has a 'farm' attribute, then return the truthiness.
        if hasattr(obj, 'farm'):
            return obj.farm.owner == request.user