from django.db import models


class Character(models.Model):

    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    birth = models.CharField(max_length=15)
    death = models.CharField(max_length=15)
    hair = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    realm = models.CharField(max_length=50)
    spouse = models.CharField(max_length=40)
