from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from moinschwein.models import Accusation

from .common import CommonTemplateView


__all__ = ['IndexView']


class IndexView(CommonTemplateView):
    page_title = _('Index')
    template_name = 'moinschwein/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super().dispatch(request, *args, **kwargs)

        return redirect(reverse('dashboard'))

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'total_accusations': Accusation.objects.count(),
        }
