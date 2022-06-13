from django.contrib import admin
from movie import models


# Register your models here.

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "year", "imdb_id", "type", "is_favorite")
