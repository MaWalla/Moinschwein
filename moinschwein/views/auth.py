from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


__all__ = ['UserLoginView', 'UserLogoutView']


class UserLoginView(LoginView):
    template_name = 'moinschwein/login.html'

    def get_success_url(self):
        return reverse('dashboard')

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'page_title': _('Login'),
        }


class UserLogoutView(LogoutView):
    next_page = 'login'
