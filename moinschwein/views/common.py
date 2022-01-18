from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


__all__ = ['CommonTemplateView', 'AuthRedirectMixin']


class CommonTemplateView(TemplateView):
    page_title = None

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'page_title': self.page_title,
        }


class AuthRedirectMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super().dispatch(request, *args, **kwargs)

        return redirect(reverse('dashboard'))
