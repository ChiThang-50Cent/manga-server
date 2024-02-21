from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import login
from knox import views as knox_views

from user.models import CustomUser
from user.serializers import CreateUserSerializer, LoginSerializer

import  rest_framework.status as status

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer

class LoginUserView(knox_views.LoginView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        
        else:
            return Response({'error' : serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(response.data, status=status.HTTP_200_OK)