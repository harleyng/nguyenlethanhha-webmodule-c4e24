import mlab
from mongoengine import Document, StringField, IntField

mlab.connect()

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

river_list_2 = River.objects(continent__contains="Africa")
river_list_3 = River.objects(continent__contains="S.America", length__lt=1000)

print("Exercise 2:")
for r in river_list_2:
    print(r.name)

print("***************************")

print("Exercise 3:")
for r in river_list_3:
    print(r.name)