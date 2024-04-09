from django.db import models
from django.contrib.auth import get_user_model


class Course(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(get_user_model(), related_name='courses')

    objects = models.Manager()

    def __str__(self):
        return self.title

