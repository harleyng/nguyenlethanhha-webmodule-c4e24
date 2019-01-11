from flask import Flask, render_template, request
from models.character import Character
import mlab

mlab.connect()
app = Flask(__name__)

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
  # 1. Get all characters (database)
    character_list = Character.objects()

  # 2. Render: template + data
    return render_template('characters.html',
                            character_list = character_list)


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



if __name__ == '__main__':
  app.run(debug=True)