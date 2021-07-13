from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import UserLoginView, UserPasswordChangeView, UserRegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password-change'),
    path('register-user/', UserRegisterView.as_view(), name='register-user'),
]
