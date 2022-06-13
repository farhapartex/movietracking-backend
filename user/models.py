from django.db import models
from django.contrib.auth import models as dj_auth_models
from core import base_models
# Create your models here.


class User(base_models.BaseAbstractModel, dj_auth_models.AbstractUser):
    rapid_api_key = models.CharField(max_length=100)

    def __str__(self):
        return self.username
