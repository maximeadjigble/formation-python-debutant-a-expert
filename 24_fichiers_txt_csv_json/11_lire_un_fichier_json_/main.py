import json

with open('data.json') as f:
    data = json.load(f)
    print(data)
    print(data['nom'])
    print(type(data['enfants']))

# data = '{ "nom": "Depp", "prenom": "Johnny", "age": 57, "enfants": true }'

# donnees = json.loads(data)
# print(donnees["nom"])
# print(donnees["prenom"])
# print(donnees["enfants"])
# # print(donnees.keys())