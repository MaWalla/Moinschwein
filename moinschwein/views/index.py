import random

from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.translation import gettext_lazy as _

from moinschwein.models import Accusation

from .common import CommonTemplateView, AuthRedirectMixin

__all__ = ['IndexView']


class IndexView(AuthRedirectMixin, CommonTemplateView):
    page_title = _('Index')
    template_name = 'moinschwein/index.html'

    def get_context_data(self, **kwargs):
        random_number = str(random.randint(1, 3)).rjust(3, '0')
        path = f'img/backgrounds/{random_number}.jpg'
        image_url = staticfiles_storage.url(path)
        return {
            **super().get_context_data(**kwargs),
            'total_accusations': Accusation.objects.count(),
            'image_url': image_url,
        }
