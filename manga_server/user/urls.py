from rest_framework.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.CreateUser.as_view(), name='create user'),
]