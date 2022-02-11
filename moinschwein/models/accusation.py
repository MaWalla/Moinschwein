from django.db import models
from django.utils import timezone
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
    timestamp = models.DateTimeField(_('timestamp'), auto_now=True)

    @property
    def local_timestamp(self):
        return timezone.localtime(self.timestamp)

    def __str__(self):
        return _('%(word)s for %(offender)s (%(offender_id)s) by %(snitch)s (%(snitch_id)s)') % {
            'word': self.word,
            'offender': self.offender.get_full_name(),
            'offender_id': self.offender.id,
            'snitch': self.snitch.get_full_name(),
            'snitch_id': self.snitch.id,
        }
