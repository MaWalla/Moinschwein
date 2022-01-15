from django.contrib import admin
from django.contrib.admin import ModelAdmin

from moinschwein.models import User


__all__ = ['UserAdmin']


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass
