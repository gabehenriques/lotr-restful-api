import json
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase
from lotr_v2.models import *


API_V2 = "/api/v2"


class APIData:
    """ Data Initializers"""

    @classmethod
    def setup_character_data(cls,
                             name="frodo baggins",
                             height='106',
                             race=None,
                             gender='male',
                             birth="ta 2968",
                             death="",
                             realm="",
                             spouse="",
                             hair="brown"
                             ):

        character = Character.objects.create(
            identifier=name,
            height=height,
            race=race,
            gender=gender,
            birth=birth,
            spouse=spouse,
            death=death,
            realm=realm,
            hair=hair
        )

        character.save()
        return character

    @classmethod
    def setup_race_data(cls,
                        name="hobbit",
                        race_type="halfling"
                        ):

        race = Race.objects.create(
            identifier=name,
            type=race_type
        )

        race.save()
        return race


class APITests(APIData, APITestCase):

    # Character Resource Tests
    def test_character_api(self):
        race = self.setup_race_data()
        character = self.setup_character_data(race=race)

        response = self.client.get(
            "{}/character/".format(API_V2)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
