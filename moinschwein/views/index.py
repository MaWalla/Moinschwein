from django.utils.translation import gettext_lazy as _

from moinschwein.models import Accusation

from .common import CommonTemplateView


__all__ = ['IndexView']


class IndexView(CommonTemplateView):
    page_title = _('Index')
    template_name = 'moinschwein/index.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'total_accusations': Accusation.objects.count(),
        }
