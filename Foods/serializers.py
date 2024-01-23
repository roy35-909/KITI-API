from rest_framework import serializers

from authentication.models import User

from .models import *


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Foods
        fields = '__all__'