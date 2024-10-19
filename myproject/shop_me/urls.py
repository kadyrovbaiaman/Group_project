from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='category_detail'),


    path('car_mark', CarMarkViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_mark_list'),
    path('car_mark/<int:pk>/', CarMarkViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='car_mark_detail'),


    path('car_model', CarModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_model_list'),
    path('car_model/<int:pk>/', CarModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                         'delete': 'destroy'}), name='car_model_detail'),
]

