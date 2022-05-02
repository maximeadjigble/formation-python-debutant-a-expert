import requests

reponse = requests.get("http://example.com")
print(reponse)
print(reponse.status_code)
print(reponse.content)