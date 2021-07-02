import requests
import json
URL = 'http://127.0.0.1:8000/StudentAPI/'

def POSTDATA():
    data = {'name':'krishna',
            'city':'belaura',
            'roll':103
            }
    jsondata = json.dumps(data)
    r = requests.post(url=URL, data=jsondata)
    res = r.json()
    print(res)

#POSTDATA()

def GETDATA(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    jsondata = json.dumps(data)
    r = requests.get(url=URL, data=jsondata)
    res = r.json()
    print(res)
GETDATA(2)

def UPDATEDATA(id):
    data = {'id':id,
            'name':'khushboo',
            'city':'delhi',
            'roll':102}
    jsondata = json.dumps(data)
    r = requests.put(url=URL, data=jsondata)
    res = r.json()
    print(res)

#UPDATEDATA(1)


def DELETEDATA(id):
    data = {'id':id}
    jsondata = json.dumps(data)

    r = requests.delete(url=URL, data=jsondata)
    res = r.json()
    print(res)

#DELETEDATA(1)