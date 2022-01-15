from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.views.generic import View

from moinschwein.models import Accusation, Word, User

from .common import CommonTemplateView


__all__ = ['DashboardView', 'LiveAccusationView']


class DashboardView(LoginRequiredMixin, CommonTemplateView):
    page_title = _('Dashboard')
    template_name = 'moinschwein/dashboard.html'

    def get_context_data(self, **kwargs):
        accusations_against_self = Accusation.objects.filter(offender=self.request.user).count()
        accusations_against_self_percentage = round((accusations_against_self / Accusation.objects.count()) * 100, 2)

        return {
            **super().get_context_data(**kwargs),
            'accusations_against_self': accusations_against_self,
            'accusations_against_self_percentage': accusations_against_self_percentage,
            'words': Word.objects.all(),
            'users': User.objects.all(),
        }


class LiveAccusationView(LoginRequiredMixin, View):
    # TODO replace this with websockets

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            [
                _('%(time)s: %(offender)s said %(word)s (reported by %(snitch)s)') % {
                    'time': accusation.timestamp.strftime('%H:%M:%S'),
                    'offender': accusation.offender.get_full_name(),
                    'word': accusation.word,
                    'snitch': accusation.snitch.get_full_name(),
                }
                for accusation in list(Accusation.objects.all())[-5:]
            ],
            safe=False,
        )
