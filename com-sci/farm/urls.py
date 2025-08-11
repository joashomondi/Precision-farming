from django.urls import path 
from .views import (
    FarmdataAPIViewset,
    CropdataAPIViewset
)

urlpatterns = [
    path('add-crop/', CropdataAPIViewset.as_view({'post': 'create'}), name='add-crop'),
    path('crop-list/', CropdataAPIViewset.as_view({'get': 'list'}), name='crop-list'),
    path('crop/<str:pk>/', CropdataAPIViewset.as_view(
            {
            'get':'retrieve', 'put':'update', 
            'patch':'partial_update', 
            'delete':'destroy'
            }), 
        name='crop-detail'),
    path('create-farm/', FarmdataAPIViewset.as_view({'post': 'create'}), name='create-farm'),
    path('farm-list/', FarmdataAPIViewset.as_view({'get': 'list'}), name='farm-list'),
    path('<str:pk>/', FarmdataAPIViewset.as_view(
            {
            'get':'retrieve', 'put':'update', 
            'patch':'partial_update', 
            'delete':'destroy'
            }), 
        name='farm-detail'),
]
