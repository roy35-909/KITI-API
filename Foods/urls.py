from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('foods',FoodViewSet.as_view(), name = "Food viewset"),
    path('foods/<int:pk>',GetFoodViewSet.as_view(), name = "Get Food viewset"),
]
