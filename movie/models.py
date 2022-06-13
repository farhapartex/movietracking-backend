from django.db import models
from django.contrib.auth import models as dj_auth_models
from core import base_models
# Create your models here.


class Movie(base_models.BaseAbstractModel):
    title = models.CharField(max_length=300)
    year = models.CharField(max_length=5)
    imdb_id = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    poster = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)
    is_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title
