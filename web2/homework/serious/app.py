import mlab
from mongoengine import Document, StringField, EmailField, DynamicField 
from flask import Flask, render_template, request
app = Flask(__name__)

mlab.connect()

class Register(Document):
    rname = StringField()
    email = EmailField()
    uname = StringField()
    psw = DynamicField()

@app.route('/')
def home():
  return "hi"

@app.route('/register', methods = ['POST', 'GET'])
def register():
  if request.method == 'POST':
    nick = request.form

    rname = nick['rname']
    email = nick['email']
    uname = nick['uname']
    psw = nick['psw']

    r = Register(rname = rname,
                email = email,
                uname = uname,
                psw = psw)
    r.save() 

    return "Welcome"
  else:
    return render_template('register.html')

  

                            

if __name__ == '__main__':
  app.run(debug=True)

