from django.contrib import admin
from . import models


@admin.register(models.Standort)
class StandortAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "land",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "pk",
        "created_at",
        "updated_at",
    )


@admin.register(models.Messwert)
class MesswertAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "wert",
        "messeinheit",
        "standort",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "pk",
        "created_at",
        "updated_at",
    )
