from django.db import models
from django.utils.translation import gettext_lazy as _


__all__ = ['Word']


class Word(models.Model):
    bad_word = models.CharField(_('bad word'), max_length=64)

    def __str__(self):
        return self.bad_word
