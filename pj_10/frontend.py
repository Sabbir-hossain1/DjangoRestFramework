import requests
import json
URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id":id}
    json_data = json.dumps(data)  
    headers = {'content-type':'application/json'}  
    r = requests.get(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
get_data()

def post_data():
    data = {
        'name': 'Rakin',
        'roll':160,
        'city':'chandpur'
    }
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.post(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
        "id":6,
        "name":'Rohit',
        "city":'Ranchi',
    }
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    res = requests.put(url=URL,headers=headers, data=json_data)
    data = res.json()
    print(data)

# update_data()

def delete_data():
    data = {"id":4}
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data=json_data)
    print(res.json())

# delete_data()
