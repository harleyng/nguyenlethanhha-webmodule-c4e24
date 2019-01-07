from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") # router 
def home(): # view function
    c = {
        "name": "AQUAMAN",
        "company": "DC COMICS",
        "image": "http://www.hottoys.com.hk/photos/PD1508471671l7j.jpg",
        "abilities": ["Speed", "Strength", "Reflexes", "Underwater", "Telepathy"]
    }
    return render_template("home.html",
                            character=c) # serve html    # response 

@app.route("/c4e")
def c4e():
    return "Code For Everyone 24"

@app.route("/hi/<name>")
def say_hi(name):
    print(name)
    return "Hi " + name

@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    total = x + y
    return str(total)



if __name__ == "__main__":
    app.run(debug=True)