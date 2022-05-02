import requests
import pyttsx3

engine = pyttsx3.init()

ville = "troyes" #valence, île-de-france
api_key = "API_KEY"

try:
    reponse = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric')
    status_code = reponse.status_code
    if status_code == 200:
        donnees = reponse.json()
        # print(donnees)
        #Température | Ressenti | Description | Humidité
        temperature = donnees["main"]["temp"]
        ressenti = donnees["main"]["feels_like"]
        description = donnees["weather"][0]["description"]
        humidite = donnees["main"]["humidity"]
        print(f"{ville} - Température: {temperature}°C, Ressenti: {ressenti}°C, Humidité: {humidite}%, Description: {description}")
        engine.say(f"The temperature in {ville} is {temperature} degrees celsius. {description}")
        engine.runAndWait()
    else:
        print("Erreur lors de la récupération des données")

except Exception as e:
    print("Une erreur s'est produite:", e)