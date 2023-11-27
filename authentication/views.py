from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

from .serializers import (
    UserRegistrationSerializer, 
    CustomTokenObtainPairSerializer, 
)
from common.renderers import CustomRenderer

User = get_user_model()

class AccountCreateView(generics.CreateAPIView):
    '''
        API endpoint for creating a customer account 
    '''
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [CustomRenderer]
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    renderer_classes = [CustomRenderer]
    
    

    