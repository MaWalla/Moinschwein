from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from moinschwein.models import User


__all__ = ['ProfileView', 'PasswordChangeView']


class UserEditForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class PasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        kwargs.pop('instance')
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'moinschwein/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile')


class PasswordChangeView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'moinschwein/password.html'
    form_class = PasswordForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('profile')
