from django.contrib import admin
from django.contrib.admin import ModelAdmin

from moinschwein.models import Word


__all__ = ['WordAdmin']


@admin.register(Word)
class WordAdmin(ModelAdmin):
    pass
