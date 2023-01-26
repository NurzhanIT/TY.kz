from django.db import models
import service
from django.contrib.postgres.fields import ArrayField

STATUS_CHOICES = [
    ('1', 'CLIENT'),
    ('2', 'ORG')
]


class User(models.Model):
    userId = models.CharField(primary_key=True)
    name = models.CharField()
    surname = models.CharField()
    password = models.CharField()
    status = models.CharField(choices=STATUS_CHOICES, default='1')
    avatar = models.ImageField(name='Avatar')
    city = models.CharField()
    # zapisi=models.CharField()


