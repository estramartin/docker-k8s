from django.urls import path
from apps.products.views import ProductViewSet, UserAPIView


urlpatterns = [   
    path('products', ProductViewSet.as_view(
        {'get': 'list',
         'post': 'create',            
         })),
    path('products/<int:pk>', ProductViewSet.as_view({
         'get': 'retrieve',
         'put': 'update',
         'patch': 'partial_update',
         'delete': 'destroy',
        })),
    path('user', UserAPIView.as_view()),
]

