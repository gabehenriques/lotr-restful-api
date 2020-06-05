from datetime import datetime as dt
from lotr_v2.models import Character
from data.helpers import build_generic

DATE_FORMAT = '%B %d, %Y'
DATA_LOCATION = "data/csv/"


def _build_characters():
    def csv_record_to_objects(info):

        yield Character(
            id=int(info[0]),
            name=str(info[6]),
            gender=str(info[3]),
            birth=str(info[1]),
            death=str(info[2]),
            hair=str(info[4]),
            height=str(info[5]),
            race=str(info[7]),
            realm=str(info[8]),
            spouse=str(info[9])
        )

    build_generic((Language,), "lotr_characters.csv", csv_record_to_objects)


def build_all():
    _build_characters()
