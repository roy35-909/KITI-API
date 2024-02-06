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


class GetFoodOrder(NewAPIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):

        """
        This API is for get all order of this user.\n

        Only For this User . Not All User.\n

        It will Provide A list of Order Which are Submited By Current User.\n

        Thank You.

        """

        objj = Order.objects.filter(user = request.user)
        ser = OrderSerializer(objj)
        return s_200(ser)


    def post(self,request):
        """
        This API is for Give a Order \n

        Here, food_id and quantity is required Field \n

        And Authentication Credintial Is required in Headers 

        Thank You.

        """
        data = request.data 

        if 'food_id' not in data:
            return s_406('food_id')
        
        if 'quantity' not in data:
            return s_406('quantity')
        

        try:
            food = Foods.objects.get(id = data['food_id'])
        except(ObjectDoesNotExist):
            return s_404("Food")
        

        objj = Order.objects.create(user = request.user, food = food, quantity = data['quantity'])

        objj.save()

        ser = OrderSerializer(objj)

        return s_200(ser)
    

class GetOrderList(NewAPIView):


    permission_classes = [IsAdminUser]


    def get(self,request):
        """
        This API is for Get List of ALL order . \n

        Only Anmin User Can Access This API.


        """

        objj = Order.objects.all().order_by('-id')

        ser = OrderSerializer(objj,many=True)

        return s_200(ser)
    

class EditOrderList(NewAPIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        """
        This API is for Retrive a Order That Own By Current User.

        """
        try:
            order = Order.objects.get(id = pk)
        except(ObjectDoesNotExist):
            return s_404('Order')
        
        ser = OrderSerializer(order)
        return s_200(ser)
    


    def post(self,request,pk):

        """
        This API is For Apcept Or Delete The order From Admin Panel.


        Provide {
        "status" : "A"    Here, "A" is For Apcept The order . And "D" is for Delete the order.
        }
        
        """

        if request.user.is_superuser == False:
            return Response({"error":"You Are Not Admin User."}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            order = Order.objects.get(id = pk)
        except(ObjectDoesNotExist):
            return s_404('Order')
        data = request.data 

        if "status" not in data:
            return s_406("status")
        
        if data["status"] == "A":
            order.status = "APCEPTED"
        
        if data["status"] == "D":

            order.status == "DELETE"
        
        order.save()

        ser = OrderSerializer(order)
        return s_200(ser)
        
    
