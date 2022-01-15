from django.contrib import admin
from django.contrib.admin import ModelAdmin

from moinschwein.models import Accusation


__all__ = ['AccusationAdmin']


@admin.register(Accusation)
class AccusationAdmin(ModelAdmin):
    pass
