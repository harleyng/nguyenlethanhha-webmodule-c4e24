from flask import Flask, render_template, request, session, redirect
from models.character import Character
from models.user import User
import mlab

app = Flask(__name__)
mlab.connect()
app.config["SECRET_KEY"] = "VadjWZvWAbLW2h9n"

# Character.objects()


@app.route('/add_character', methods = ['GET', 'POST'])
def add_character():
  # 1: Gui form (GET)
  if request.method == "GET":
    return render_template('character_form.html')
  elif request.method == "POST":
  # 4: Nhan form => luu
    form = request.form 
    name = form["name"]
    image = form["image"]
    rate = form["rate"]
    new_character = Character(name=name, image=image, rate=rate)
    new_character.save()
    return "Gotcha"
  
# list (master)
@app.route('/characters') # hien thi tat ca cac nhan vat
def characters():
  if "token" in session:
    # 1. Get all characters (database)
      character_list = Character.objects()

    # 2. Render: template + data
      return render_template('characters.html',
                              character_list = character_list)
  else:
    return redirect("/login?next=/characters") # ?next=/characters


@app.route('/character/<given_id>')
def character_detail(given_id): # one
  # 1. Get one character, based on given id 
  # character = Character.objects(id=given_id).first() 
  character = Character.objects().with_id(given_id)
  if character is None:
    return "Not found"
  else: # 2. Render: template + data
    return render_template("character_detail.html", character = character)

@app.route('/update/<given_id>', methods = ['GET', 'POST'])
def update(given_id):
  character = Character.objects().with_id(given_id)
  if character is None:
    return "Not found"
  else:
    if request.method == 'GET':
      return render_template('update_character.html')
    else:
      form = request.form 
      name = form["name"]
      image = form["image"]
      rate = form["rate"]
      if name != "":
        character.update(set__name=name)
      if image != "":
        character.update(set__image=image)
      if rate != "":
        character.update(set__rate=rate)
      return "Update Success"

@app.route('/delete/<given_id>')
def delete(given_id):
  character = Character.objects().with_id(given_id)
  if character is None:
    return "Not found"
  else:
    character.delete()
    return "Delete Success"

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login_form.html')
  else:
    form = request.form 
    username = form['username']
    password = form['password']

    found_user = User.objects(username=username).first()
    if found_user is None:
      return "User not found"
    elif found_user.password != password:
      return "Invalid password"
    else: 
      session['token'] = username
      next = request.args.get("next")
      if next is None or next == "":
        return "Logged in successfully"
      else:
        return redirect(next)

@app.route("/posts")
def posts():
  if "token" not in session:
    return redirect("/login?next=/posts")
  else:
    username = session["token"]

@app.route("/logout")
def logout():
  del session["token"]
  return redirect("/login")

if __name__ == '__main__':
  app.run(debug=True)