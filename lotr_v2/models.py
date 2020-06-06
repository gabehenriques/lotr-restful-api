from django.db import models


class Character(models.Model):

    name = models.CharField(max_length=60, default=None)

    height = models.FloatField(null=True, blank=True, default=None)

    race = models.CharField(max_length=20, default=None)

    gender = models.CharField(max_length=10, default=None)

    birth = models.CharField(max_length=30, default=None)

    spouse = models.CharField(max_length=70, default=None)

    death = models.CharField(max_length=30, default=None)

    realm = models.CharField(max_length=90, default=None)

    hair = models.CharField(max_length=20, default=None)

    wiki = models.CharField(max_length=90, default=None)
