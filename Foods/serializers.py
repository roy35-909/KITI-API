from rest_framework import serializers

from authentication.models import User
from authentication.serializers import UserProfileSerializer

from .models import *


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Foods
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    food = FoodSerializer()
    user = UserProfileSerializer()
    class Meta:
        model = Order
        fields = '__all__'