from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User


class UserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email','password']


class UserProfileSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email','role']


    def get_role(self,instance):

        if instance.is_superuser:
            return True 
        else:
            return False

class UserSerializerWithToken(UserCreationSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['token']
        
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
