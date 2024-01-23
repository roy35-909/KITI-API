from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register',RegisterAPIVIEW.as_view(), name="Register APIView"),
]
