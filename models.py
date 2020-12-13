# importing from peewee using *).

from peewee import *
import datetime

# Connects to Postgres database
DATABASE = PostgresqlDatabase('teacher_genie_app', host='localhost', port=5432)

createdb teacher_genie_app


class Student(Model):
    id = CharField()
    name = CharField()
    registered_courses = CharField()
    email = CharField()
    balance_due = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

# "safe=True" = If set to true then the table
    # will only be created if it doesn't already exist.


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Student], safe=True)
    print("TABLES CREATED")
    DATABASE.close()
