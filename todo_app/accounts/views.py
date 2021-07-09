from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('tasks')
