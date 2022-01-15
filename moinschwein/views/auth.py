from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse


__all__ = ['UserLoginView', 'UserLogoutView']


class UserLoginView(LoginView):
    template_name = 'moinschwein/login.html'

    def get_success_url(self):
        return reverse('dashboard')


class UserLogoutView(LogoutView):
    next_page = 'login'
