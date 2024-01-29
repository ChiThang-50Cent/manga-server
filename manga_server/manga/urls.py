from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.MangaListView.as_view(), name='Retrieve all manga'),
    path('<int:manga_id>/', view=views.MangaDetailAPI, name='Retrieve manga detail'),
    path('<int:manga_id>/chapter/<int:chapter_id>/', view=views.ChapterDetailAPI, name='Retrieve chapter detail'),
    path('create_manga/', view=views.MangaCreateView.as_view(), name='Create manga'),
    path('add_chapter/', view=views.ChapterCreateView.as_view(), name='Add chapter'),
]