from django.urls import path

from . import views

urlpatterns = [
    path('create_manga/', view=views.MangaCreateView.as_view(), name='Create manga'),
    path('upload/', views.upload_chapter, name='upload'),
]