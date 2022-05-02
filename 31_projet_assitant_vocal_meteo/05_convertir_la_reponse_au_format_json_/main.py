import requests

ville = "île-de-france"
api_key = "API_KEY"

try:
    reponse = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric')
    status_code = reponse.status_code
    if status_code == 200:
        donnees = reponse.json()
        print(donnees)
    else:
        print("Erreur lors de la récupération des données")

except Exception as e:
    print("Une erreur s'est produite:", e)