from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.views import View

from moinschwein.models import Accusation, User

from .common import CommonTemplateView


__all__ = ['StatisticView', 'StatisticDataView']


class StatisticView(LoginRequiredMixin, CommonTemplateView):
    page_title = _('Statistics')
    template_name = 'moinschwein/statistic.html'


class StatisticDataView(LoginRequiredMixin, View):
    template_name = 'moinschwein/profile.html'

    def get(self, *args, **kwargs):
        user_ids = User.objects.values_list('id', flat=True)

        accused = User.objects.annotate(
            amount=Count('offender_accusations'),
        ).order_by(
            'amount',
        ).values(
            'amount',
            'id',
            'first_name',
            'last_name',
        )

        # for some reason I have to annotate each count in a seperate query or the number goes wild
        accusing = User.objects.annotate(
            amount=Count('snitch_accusations'),
        ).order_by(
            'amount',
        ).values(
            'amount',
            'id',
            'first_name',
            'last_name',
        )

        return JsonResponse({
            'user_ids': list(user_ids),
            'accused': list(accused),
            'accusing': list(accusing),
        })
