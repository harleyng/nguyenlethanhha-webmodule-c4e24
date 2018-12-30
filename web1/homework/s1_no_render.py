from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<int:w>/<int:h>')
def BMI(w, h):
  w = w * 10000
  BMI = w / (h * h) 
  if BMI < 16:
    return "Severely underweight"
  elif BMI < 18.5: 
    return "Underweight"
  elif BMI < 25:
    return "Normal"
  elif BMI < 30:
    return "Overweight"
  else:
    return "Obese"
  

if __name__ == '__main__':
  app.run(debug=True)