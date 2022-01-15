from django.views.generic import TemplateView


__all__ = ['CommonTemplateView']


class CommonTemplateView(TemplateView):
    page_title = None

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'page_title': self.page_title,
        }
