from datetime import datetime as dt
from lotr_v2.models import Character, Race
from data.helpers import build_generic

DATE_FORMAT = '%B %d, %Y'
CHARACTERS_FILE = "lotr_characters.csv"
RACE_FILE = "lotr_races.csv"


def _build_characters():
    def csv_record_to_objects(info):

        yield Character(
            identifier=str(info[0]),
            height=float(info[1]),
            race_id=int(info[2]),
            gender=str(info[3]),
            birth=str(info[4]),
            spouse=str(info[5]),
            death=str(info[6]),
            realm=str(info[7]),
            hair=str(info[8])
        )

    build_generic((Character,), CHARACTERS_FILE, csv_record_to_objects)


def _build_races():
    def csv_record_to_objects(info):

        yield Race(
            identifier=str(info[0]),
            type=str(info[1])
        )

    build_generic((Race,), RACE_FILE, csv_record_to_objects)


def build_all():
    _build_characters()
    # _build_races()
