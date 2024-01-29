from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response

from user.models import CustomUser
from user.serializers import RegisterSerializer
# Create your views here.

class CreateUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
