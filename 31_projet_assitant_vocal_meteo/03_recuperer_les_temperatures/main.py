import requests

ville = "île-de-france"
api_key = "API_KEY"

try:
    reponse = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric')
    print(reponse)
except Exception as e:
    print("Une erreur s'est produite:", e)