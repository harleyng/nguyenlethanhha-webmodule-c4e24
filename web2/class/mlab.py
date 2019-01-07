import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds239968.mlab.com:39968/moviedb
host = "ds239968.mlab.com"
port = 39968
db_name = "moviedb"
user_name = "admin1"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())