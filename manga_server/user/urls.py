from rest_framework.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create user'),
]