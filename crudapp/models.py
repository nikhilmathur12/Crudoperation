from django.db import models


class Data(models.Model):
    country = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.name
