from authentication.base_response import *
from authentication.models import User
from authentication.modified_api_view import *
from authentication.serializers import *
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value
        # Remove access and Refresh Token Form representation
        data.pop('access')
        data.pop('refresh')
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class RegisterAPIVIEW(NewAPIView):
    serializer_class = UserCreationSerializer
    def post(self,request):

        data = request.data 

        required_fields = ['email','first_name','last_name','password']

        for i in required_fields:
            if i not in data:
                return s_406(i)
            
        user = User.objects.create(email = data['email'], first_name = data['first_name'], last_name = data['last_name'])
        user.set_password(data['password'])
        user.save()
        ser = UserProfileSerializer(user)
        return s_200(ser)
    