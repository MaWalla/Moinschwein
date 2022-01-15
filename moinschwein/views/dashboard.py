from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


__all__ = ['DashboardView']


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'moinschwein/dashboard.html'
