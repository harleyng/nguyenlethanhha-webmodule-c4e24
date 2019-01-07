import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds151354.mlab.com:51354/register
host = 'ds151354.mlab.com'
port = 51354
db_name = 'register'
user_name = 'admin'
password = 'admin1'


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())