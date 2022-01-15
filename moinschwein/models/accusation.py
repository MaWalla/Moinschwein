from django.db import models
from django.utils.translation import gettext_lazy as _

from .user import User
from .word import Word


__all__ = ['Accusation']


class Accusation(models.Model):
    offender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='offender_accusations',
        verbose_name=_('offender'),
    )
    snitch = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='snitch_accusations',
        verbose_name=_('snitch'),
    )
    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
        related_name='accusations',
        verbose_name=_('word'),
    )
