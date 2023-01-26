from django.db import models
from django.contrib.postgres.fields import ArrayField


class Gallery(models.Model):
    photo = ArrayField(
        models.ImageField(),
        max_length=10,
    )
