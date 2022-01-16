from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, CreateView

from moinschwein.models import Accusation


__all__ = ['SubmitAccusationView']


class SubmitAccusationForm(ModelForm):

    class Meta:
        model = Accusation
        fields = '__all__'


class SubmitAccusationView(LoginRequiredMixin, FormView):
    form_class = SubmitAccusationForm
    
    def form_valid(self, form):
        instance = Accusation.objects.create(**form.cleaned_data)
        instance.save()
        return JsonResponse({'id': instance.id}, status=200)
    
    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)
