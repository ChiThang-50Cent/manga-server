from rest_framework.urls import path
from . import views
from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path('create_user/', views.CreateUserView.as_view(), name='create user'),
    path('login/', views.LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutView.as_view(), name='logout user'),
    path('logout-all/', LogoutAllView.as_view(), name='logout all user'),
]