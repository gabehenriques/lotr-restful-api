from datetime import datetime as dt
from lotr_v2.models import Character
from data.helpers import build_generic

DATE_FORMAT = '%B %d, %Y'
FILE = "lotr_characters.csv"


def _build_characters():
    def csv_record_to_objects(info):

        yield Character(
            name=str(info[0]),
            height=float(info[1]),
            race=str(info[2]),
            gender=str(info[3]),
            birth=str(info[4]),
            spouse=str(info[5]),
            death=str(info[6]),
            realm=str(info[7]),
            hair=str(info[8]),
            wiki=str(info[9])
        )

    build_generic((Character,), FILE, csv_record_to_objects)


def build_all():
    _build_characters()
