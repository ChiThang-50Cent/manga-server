from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from knox.auth import TokenAuthentication

from . import serializers
from .models import Chapter, Manga
from permissions import IsUploaderPermission, IsChapterOwnerPermission, IsMangaOwnerPermission

# Create your views here.

"""
 For Manga View
"""
# GET Manga
class MangaListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]

    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer

class MangaDetailRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]

    queryset = Manga.objects.all()
    serializer_class = serializers.MangaDetailSerializer

# CRUD Manga
class MangaCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsUploaderPermission, ]

    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer

class MangaDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsMangaOwnerPermission, ]

    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer

# For Chapter View
class ChapterCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsUploaderPermission, ]

    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer

class ChapterDetailRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]

    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterDetailSerializer

class ChapterDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsChapterOwnerPermission, ]

    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer