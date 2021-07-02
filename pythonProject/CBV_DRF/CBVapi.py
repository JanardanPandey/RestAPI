import requests
import json


URL = " http://127.0.0.1:8000/StudentAPI/"

def getdata(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    jsondata = json.dumps(data)
    r = requests.get(url=URL, data=jsondata)
    res = r.json()
    print(res)

#getdata()

def postdata():
    data = {'name':'rishna',
            'city':'patisa',
            'roll':5
            }
    jsondata = json.dumps(data)
    r = requests.post(url=URL,data=jsondata)
    res = r.json()
    print(res)

postdata()

def put():
    data = {'id':2,
            'name':'madhusudan'
            }
    jsondata = json.dumps(data)
    r = requests.put(url=URL, data=jsondata)
    res = r.json()
    print(res)

#put()
def delete():
    data = {'id':2}
    jsondata = json.dumps(data)
    r = requests.delete(url=URL, data=jsondata)
    res = r.json()
    print(res)

#delete()