from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def create_user(request):
    print(request)
    return Response({"Hi" : "Hi"})
