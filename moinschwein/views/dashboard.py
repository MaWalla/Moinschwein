from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _

from .common import CommonTemplateView


__all__ = ['DashboardView']

from ..models import Accusation


class DashboardView(LoginRequiredMixin, CommonTemplateView):
    page_title = _('Dashboard')
    template_name = 'moinschwein/dashboard.html'

    def get_context_data(self, **kwargs):
        accusations_against_self = Accusation.objects.filter(offender=self.request.user).count()

        return {
            **super().get_context_data(**kwargs),
            'accusations_against_self': accusations_against_self,
        }
