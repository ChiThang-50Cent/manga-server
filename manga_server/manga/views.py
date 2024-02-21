from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from . import serializers
from .models import Chapter, Manga

import rest_framework.status as status
from manga import utils as m_utils

# Create your views here.

class MangaCreateAPIView(generics.CreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer

class MangaListAPIView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer

class ChapterCreateAPIView(generics.CreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer

class MangaDetailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Manga.objects.all()
    serializer_class = serializers.MangaDetailSerializer

class ChapterDetailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterDetailSerializer
