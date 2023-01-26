from user.models import User
from gallery.models import Gallery
from django.db import models
import service


class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orgName = models.CharField()
    orgAvatar = models.ImageField(name='orgAvatar')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    @staticmethod
    def rating(self):
        service.compute_rating()


class Rating_number(models.Model):
    star = models.IntegerField()
