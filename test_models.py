from mongoengine import *


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Qoutes(Document):
    tags = ListField()
    author = StringField()
    quote = StringField()
