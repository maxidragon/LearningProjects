import json
path = r'C:\Users\Max\PycharmProjects\Informatyka\files/data.json'
data = {
  "id": 5,
  "name": "Chelsey Dietrich",
  "username": "Kamren",
  "email": "Lucio_Hettinger@annie.ca",
    "working":False,
  "address": {
    "street": "Skiles Walks",
    "suite": "Suite 351",
    "city": "Roscoeview",
    "zipcode": "33263",
    "geo": {
      "lat": "-31.8129",
      "lng": "62.5342"
    }}}
#with open(path, 'w', encoding='utf-8') as file:
#  json.dump(data, file)

with open(path, 'r', encoding='utf-8') as file:
  content = json.load(file)
  print(content['address']['geo'])
