from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def home():
    me = {
        "name": "Harley",
        "work": "Student",
        "school": "University of Technology and Science of Hanoi",
        "hobbies": "dancing, reading, doing excersises, playing video games"
    }
    return render_template("portfolio.html", me=me)


@app.route('/school')
def school():
    return redirect("http://techkids.vn", code = 302)

if __name__ == '__main__':
  app.run(debug=True)