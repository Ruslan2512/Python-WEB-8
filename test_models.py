from mongoengine import *

connect(host="mongodb+srv://ruslan:qwerty123@cluster.9diyzhg.mongodb.net/?retryWrites=true&w=majority")


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Qoutes(Document):
    tags = ListField()
    author = StringField()
    quote = StringField()
