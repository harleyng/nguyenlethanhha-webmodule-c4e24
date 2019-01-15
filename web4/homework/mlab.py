import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds157574.mlab.com:57574/bike
host = 'ds157574.mlab.com'
port = 57574
db_name = 'bike'
user_name = 'admin1'
password = 'admin1'


def connect():
   mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
   import json
   return [json.loads(item.to_json()) for item in l]


def item2json(item):
   import json
   return json.loads(item.to_json())