from django.contrib import admin

from inventory.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
