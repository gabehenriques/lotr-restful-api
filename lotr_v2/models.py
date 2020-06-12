from django.db import models


class HasName(models.Model):

    identifier = models.CharField(max_length=100, db_index=True, default=None)

    class Meta:
        abstract = True


class HasCharacter(models.Model):

    character = models.ForeignKey(
        "Character",
        blank=True,
        null=True,
        related_name="%(class)s",
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class HasRace(models.Model):

    race = models.ForeignKey(
        "Race",
        blank=True,
        null=True,
        related_name="%(class)s",
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Character(HasName, HasRace):

    height = models.FloatField(null=True, blank=True, default=None)

    gender = models.CharField(max_length=10, default=None)

    birth = models.CharField(max_length=30, default=None)

    spouse = models.CharField(max_length=70, default=None)

    death = models.CharField(max_length=30, default=None)

    realm = models.CharField(max_length=90, default=None)

    hair = models.CharField(max_length=20, default=None)

    def __str__(self):
        return '%s: ' % (self.identifier)


class Race(HasName):
    type = models.CharField(max_length=50, default=None)
