from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


__all__ = ['User']


class User(AbstractUser):

    def __str__(self):
        return _('%(full_name)s (%(username)s)') % {
            'full_name': self.get_full_name(),
            'username': self.username,
        }
