from rest_framework import serializers

from .models import *


class RaceSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race
        fields = ("identifier", "url")


class CharacterSummarySerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField('get_character_name')

    class Meta:
        model = Character
        fields = ("name", "url")

    def get_character_name(self, obj):
        return obj.identifier


class RaceDetailSerializer(serializers.ModelSerializer):

    character = CharacterSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Race
        fields = ("identifier", "character")


class CharacterDetailSerializer(serializers.ModelSerializer):

    race = serializers.HyperlinkedIdentityField(view_name='race-detail')

    class Meta:
        model = Character
        fields = ("id", "identifier", "height", "race", "gender", "birth",
                  "spouse", "death", "realm", "hair", "race")
