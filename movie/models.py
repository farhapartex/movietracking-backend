from django.db import models
from django.contrib.auth import models as dj_auth_models
from core import base_models
from user import models as user_models
# Create your models here.


class Movie(base_models.BaseAbstractModel):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name="movies", null=True)
    title = models.CharField(max_length=300)
    year = models.CharField(max_length=5)
    imdb_id = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    poster = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)
    is_watched = models.BooleanField(default=False)
    rated = models.CharField(max_length=50, blank=True, null=True)
    runtime = models.CharField(max_length=50, blank=True, null=True)
    genre = models.CharField(max_length=200, blank=True, null=True)
    director = models.CharField(max_length=500, blank=True, null=True)
    writer = models.CharField(max_length=500, blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    awards = models.CharField(max_length=200, blank=True, null=True)
    released = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
