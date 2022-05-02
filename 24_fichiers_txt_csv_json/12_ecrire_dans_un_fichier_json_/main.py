import json

data = { "nom": "Depp", "prenom": "Johnny", "age": 57, "enfants": True }
print(type(data))
print(data['prenom'])
 
# data = json.dumps(data)
# print(type(data))
# print(data)

with open('data.json', "w") as f:
    json.dump(data, f)