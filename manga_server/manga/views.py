from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import Chapter, Manga
from .serializers import MangaSerializer, ChapterSerializer

import rest_framework.status as status
import manga.utils as u

# Create your views here.

@api_view(['GET'])
def upload_chapter(request):
    chapter = Chapter.objects.get(id=2)

    res = u.upload_chapter_from_local(chapter)

    return Response(res, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_chapter(request):

    chapter = Chapter.objects.get(id=2)

    res = u.get_all_page_from_chapter(chapter)

    return Response(res, status=status.HTTP_200_OK)

class MangaCreateView(CreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

class ChapterCreateView(CreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer