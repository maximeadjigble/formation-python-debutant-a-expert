# prix = 25

# if prix < 10:
#     print("Ok, j'achète")
# elif prix >= 10 and prix <= 20:
#     print("Je vais y réfléchir")
# else:
#     print("Le prix est élevé")

# print("Fin")


username = "Claude" 
users = ["Romaric","Hugo","Benois","Clement"]
admins = ["François", "Claude"]

if username in users: 
    print("Bienvenue", username)
elif username in admins:
    print("Bienvenue dans l'interface administrateur")
else: 
    print(f"Cette page n'est pas accéssible")

print("Fin")