from rest_framework import serializers

from .models import *


class CharacterDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ("id", "name", "height", "race", "gender", "birth",
                  "spouse", "death", "realm", "hair", "wiki")
