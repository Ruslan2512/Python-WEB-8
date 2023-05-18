from mongoengine import *

# connect(host="mongodb+srv://ruslan:qwerty123@web8.r3yh7e7.mongodb.net/?retryWrites=true&w=majority", ssl=True)


class Author(EmbeddedDocument):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Qoutes(EmbeddedDocument):
    tags = ListField()
    author = StringField()
    quote = StringField()
