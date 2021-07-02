import requests
import json

URL ='http://127.0.0.1:8000/student_api/'
def GETDATA(id = None):
    data= {}
    if id is not None:
        data = {'id':id}
    jsondata = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r  = requests.get(url=URL, headers=headers,  data = jsondata)
    res = r.json()
    print(res)

#GETDATA(1)\

def POSTDATA():
    data = {
        'name':'khusnhboo',
        'city':'pandey',
        'roll':104
    }
    jsondata = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.post(url=URL, headers=headers , data= jsondata)
    res = r.json()
    print(res)

POSTDATA()

def UPDATEDATA():
    data = {
        'id':1 ,
        'name':'Khushboo',
        'city':'gorakhpur'
    }
    jsondata  = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.put(url=URL, headers= headers , data = jsondata)
    res = r.json()
    print(res)
#UPDATEDATA()

def DELETEDATA(id):
    data = {
        'id':id
        }
    jsondata = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.delete(url=URL, headers=headers, data = jsondata)
    res = r.json()
    print(res)

#DELETEDATA(1)