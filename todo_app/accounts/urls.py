from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import UserPasswordChangeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password-change'),
]
