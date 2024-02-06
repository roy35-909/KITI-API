from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('foods',FoodViewSet.as_view(), name = "Food viewset"),
    path('foods/<int:pk>',GetFoodViewSet.as_view(), name = "Get Food viewset"),


    # Food Order

    path('submit_order',GetFoodOrder.as_view(),name = "Get Food Order"),
    path('get_order_list',GetOrderList.as_view(),name = "Get Order List"),
    path('get_order_list',GetOrderList.as_view(),name = "Get Order List"),

    path('change_status/<int:pk>', EditOrderList.as_view(),name = "Edit Order Status"),
]
