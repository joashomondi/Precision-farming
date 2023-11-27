from django.urls import path, include
from .views import (
    AccountCreateView,
    CustomTokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter


app_name = "authentication"


urlpatterns = [
    # regular urls
    path('sign-up/', AccountCreateView.as_view(), name='create-account'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]
