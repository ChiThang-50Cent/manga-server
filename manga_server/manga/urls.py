from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.MangaListAPIView.as_view(), name='Retrieve all manga'),
    path('<int:pk>/', view=views.MangaDetailRetrieveAPIView.as_view(), name='Retrieve manga detail'),
    path('<int:manga_id>/chapter/<int:pk>/', view=views.ChapterDetailRetrieveAPIView.as_view(), name='Retrieve chapter detail'),
    path('create_manga/', view=views.MangaCreateAPIView.as_view(), name='Create manga'),
    path('add_chapter/', view=views.ChapterCreateAPIView.as_view(), name='Add chapter'),
]