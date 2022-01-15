from django.forms import ModelForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from moinschwein.models import Accusation


__all__ = ['SubmitAccusationView']


class SubmitAccusationForm(ModelForm):

    class Meta:
        model = Accusation
        fields = '__all__'


class SubmitAccusationView(CreateView):
    form_class = SubmitAccusationForm
    success_url = reverse_lazy('dashboard')
