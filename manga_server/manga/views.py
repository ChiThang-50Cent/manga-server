from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from . import serializers
from .models import Chapter, Manga

import rest_framework.status as status
from manga import utils as m_utils

# Create your views here.

class MangaCreateView(generics.CreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer

class MangaListView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer

class ChapterCreateView(generics.CreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer

@api_view(['GET'])
def MangaDetailAPI(request, manga_id):
    try:
        manga = Manga.objects.get(pk=manga_id)
        seria = serializers.MangaDetailSerializer(manga)

        return Response(seria.data, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Error" : str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])

def ChapterDetailAPI(request, manga_id, chapter_id):
    try:
        chapter = Chapter.objects.get(pk=chapter_id)
        seria = serializers.ChapterDetailSerializer(chapter)

        return Response(seria.data, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Error" : str(ex)}, status=status.HTTP_400_BAD_REQUEST)