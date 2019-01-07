# 1. connect to databas
import mlab 
from mongoengine import Document, StringField, IntField

mlab.connect()

# 2. define model
class Movie(Document):  
    title = StringField()
    image = StringField()
    link = StringField()
    rate = IntField()


movie_list = Movie.objects(rate__gte=7, title_icontains="Aquaman") #Lazy Loading
for m in movie_list:
    print(m.title, m.rate)

# # 3. create data
# m = Movie(title="Scooby-Doo",
#           image = "https://m.media-amazon.com/images/M/MV5BMTg4MzMzMTY0OF5BMl5BanBnXkFtZTYwNzM3MTg2._V1_UX182_CR0,0,182,268_AL_.jpg",
#           link = "https://www.imdb.com/title/tt0267913/?ref_=adv_li_tt",
#           rate = 5)

# m.save()