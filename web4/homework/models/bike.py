from mongoengine import Document, StringField, IntField

class Bike(Document):
    model = StringField()
    fee = IntField()
    image = StringField()
    year = IntField()

