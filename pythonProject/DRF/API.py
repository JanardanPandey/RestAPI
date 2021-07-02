import requests
import json


URL = 'http://127.0.0.1:8000/api/'

def POST_DATA():
    data = {'name':'Khushboo',
            'city':'Delhi',
            'roll':103
            }
    jsonData = json.dumps(data)
    r = requests.post(url=URL, data=jsonData)
    data = r.json()
    print(data)

#POST_DATA()

def UPDATE_DATA():
    Data = {
        'id': 2,
        'name' : 'Madhusudan',
        'roll': 102
    }

    jsondata = json.dumps(Data)
    r = requests.put(url=URL, data=jsondata)
    data = r.json()
    print(data)

#UPDATE_DATA()

def GET_DATA(id = None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL , data = json_data)
    data = r.json()
    print(data)

#n = input("Please enter student ID")
#if n != '':
    #GET_DATA(n)
#else:
    #GET_DATA()
GET_DATA()

def DELETE_DATA(n):
    data = {'id':n}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    res = r.json()
    print(res)

#DELETE_DATA(input('Please Enter deleted data ID'))





