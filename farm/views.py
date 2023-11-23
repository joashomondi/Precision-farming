from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.validators import ValidationError 
from django_auto_prefetching import AutoPrefetchViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from common.renderers import CustomRenderer 
from common import permissions as custom_permissions
from .serializers import FarmDataSerializer, CropDataSerializer
from .models import FarmData, CropData
# Create your views here.

class FarmdataAPIViewset(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = FarmDataSerializer 
    queryset = FarmData.objects.all()
    renderer_classes = [CustomRenderer]
    
    
    def get_queryset(self):
    # define queryset for staff and normal users
    
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(owner__is_active=True)
    
    def get_permissions(self):
        # define permissions based on the action a user wants to perform
        
        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [custom_permissions.IsOwnerOrReadOnly]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()
    
    
    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError:
            raise ValidationError(
                                    {
                                    "detail": "A Farm with this name has already been created."
                                    }
                                )


class CropdataAPIViewset(AutoPrefetchViewSetMixin, ModelViewSet):
    serializer_class = CropDataSerializer 
    queryset = CropData.objects.all()
    renderer_classes = [CustomRenderer]
    
    def get_queryset(self):
    # define queryset for staff and normal users
    
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(farm__owner__is_active=True)
    
    def get_permissions(self):
        # define permissions based on the action a user wants to perform
        
        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [custom_permissions.IsOwnerOrReadOnly]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()
    
    
    def perform_create(self, serializer):
        crop = CropData.objects.filter(farm__owner=self.request.user)     
        if not crop.exists():
            serializer.save()
        else:
            raise ValidationError(
                                    {
                                    "detail": "A Crop with this name has been added to this Farm"
                                    }
                                )
            