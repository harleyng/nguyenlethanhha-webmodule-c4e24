from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:w>/<int:h>')
def BMI(w, h):
    table = {
        "1": "Severely underweight",
        "2": "Underweight",
        "3": "Normal",
        "4": "Overweight",
        "5": "Obese"
    }

    w = w * 10000
    BMI = w / (h * h) 
    return render_template("calc_bmi.html", table=table, BMI=BMI)
  

if __name__ == '__main__':
  app.run(debug=True)