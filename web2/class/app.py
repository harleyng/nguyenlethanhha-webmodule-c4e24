from flask import Flask, render_template
app = Flask(__name__)

@app.route('/characters')
def characters():
    c_list = [
        {
        "name": "Thanos",
        "image": "https://www.sideshowtoy.com/wp-content/uploads/2018/04/marvel-avengers-infinity-war-thanos-sixth-scale-figure-hot-toys-feature-903429-1.jpg",
        "link": "https://en.wikipedia.org/wiki/Thanos"
    },
    {
        "name": "Captain America",
        "image": "http://assets.readbrightly.com/wp-content/uploads/2016/05/captain-america-feat.jpg",
        "link": "https://en.wikipedia.org/wiki/Captain_America"
    },
    {
        "name": "Spiderman",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7YdZvjUvsdf-D96Do5bDOTjZWybL1-0h-0-ET7FDcU5eSUUTV7Q",
        "link": "https://en.wikipedia.org/wiki/Spider-Man"
    }
    ]
    return render_template("character_list.html",
                            character_list=c_list)

@app.route('/names')
def names():
    name_list = ["Huy", "Quoc", "Huong", "Tung"]
    return render_template("name.html",
                            name_list=name_list)

food_list = [
    {
        "name": "Bún riêu",
        "image": "https://tea-1.lozi.vn/v1/images/resized/bun-rieu-cua-134109-1449025952?w=960&type=o",
        "link": "https://lozi.vn/b/ngo-55-hai-ba-trung-1449025952?utm_campaign=copy",
        "ytid": "rYD0fh7L1r4"
    },
    {
        "name": "Bún đậu mắm tôm",
        "image": "https://images.foody.vn/res/g3/28879/prof/s576x330/foody-mobile-bun-dau-viet-ha-noi.jpg",
        "link": "https://www.foody.vn/ha-noi/bun-dau-viet",
         "ytid": "jWYCxomF7lo"
    },
    {
        "name": "Bún ngan",
        "image": "https://images.foody.vn/res/g70/693326/prof/s576x330/foody-mobile-22045769_11798535521-134-636431573959949453.jpg",
        "link": "https://www.foody.vn/ha-noi/ba-hang-bun-ngan-bun-tron",
         "ytid": "rHbHunacl0"
    }
    ]
    
@app.route('/food_items')
def food_items():
    return render_template("food.html",
                            food_list=food_list)

@app.route('/food_detail/<int:index>')
def food_detail(index):
    food = food_list[index]
    return render_template('food_detail.html',
                            food = food)

if __name__ == '__main__':
  app.run(debug=True)