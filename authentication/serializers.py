from authentication.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email','password']


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email']


class UserSerializerWithToken(UserCreationSerializer):
    token = serializers.SerializerMethodField(read_only=True)
   
    class Meta:
        model = User
        fields = ['token']
        
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
