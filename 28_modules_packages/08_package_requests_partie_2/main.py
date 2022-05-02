import requests

reponse = requests.get('http://api.open-notify.org/astros.json')
# print(reponse)
if reponse.status_code == 200:
    # print(type(reponse.content))
    # print(type(reponse.json()))
    donnees = reponse.json()
    message = donnees['message']
    nombre = donnees['number']
    personnes = donnees['people']
    print(message)
    print(nombre)
    print(personnes)
else:
    print("Erreur dans la requette")