from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.base_response import *
from authentication.models import User
from authentication.modified_api_view import *
from authentication.serializers import *

from .models import *
from .serializers import *


class FoodViewSet(ListAPIView):
    """
    You can Get a List of Food Here

    Thanks .
    """
    queryset = Foods.objects.all()
    serializer_class = FoodSerializer
    permission_classes = []


class GetFoodViewSet(RetrieveAPIView):
    """
    You need use it When You need a Specific Food Details . 
    \n
    Send A Get Request With Food Id .

    Thanks.
    """
    queryset = Foods.objects.all()
    serializer_class = FoodSerializer
    permission_classes = []