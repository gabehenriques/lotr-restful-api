import csv
import os
import os.path
import re
import json
from django.db import connection

DB_CURSOR = connection.cursor()
DB_VENDOR = connection.vendor
DATA_LOCATION = "data/csv/"


def with_iterable(context, iterable=None):
    if iterable is None:
        iterable = context
    with context:
        for value in iterable:
            yield value


def load_data(file_name):
    return csv.reader(
        with_iterable(open(DATA_LOCATION + file_name, "rt", encoding="utf8")),
        delimiter=","
    )


def clear_table(model):
    table_name = model._meta.db_table
    model.objects.all().delete()
    if DB_VENDOR == "sqlite":
        DB_CURSOR.execute(
            "DELETE FROM sqlite_sequence WHERE name = " + "'" + table_name + "'"
        )
    else:
        DB_CURSOR.execute(
            "SELECT setval(pg_get_serial_sequence("
            + "'"
            + table_name
            + "'"
            + ",'id'), 1, false);"
        )


def build_generic(model_classes, file_name, csv_record_to_objects):
    batches = {}
    for model_class in model_classes:
        clear_table(model_class)
        batches[model_class] = []

    csv_data = load_data(file_name)
    next(csv_data, None)

    for csv_record in csv_data:
        for obj in csv_record_to_objects(csv_record):
            model_class = type(obj)
            batches[model_class].append(obj)

            if len(batches[model_class]) > 200:
                model_class.objects.bulk_create(batches[model_class])
                batches[model_class] = []

    for model_class, batch in batches.items():
        model_class.objects.bulk_create(batch)
