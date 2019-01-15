from flask import Flask, render_template, request
from models.bike import Bike 
import mlab 



app = Flask(__name__)

mlab.connect()

@app.route('/new_bike', methods =['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('new_bike_form.html')
    else:
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]

        bike_sample = Bike(model=model, fee=fee, image=image, year=year)
        bike_sample.save()
        return "Hurrayyy"


if __name__ == '__main__':
  app.run(debug=True)