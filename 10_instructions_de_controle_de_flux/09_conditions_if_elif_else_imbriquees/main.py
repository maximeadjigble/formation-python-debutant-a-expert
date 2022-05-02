age = 36
nom = "Maxime"
membres = ["Jean", "Pierre", "Raissa", "Claudette"]

if age >= 18:
    print("Vous avez le droit d'acheter de l'alchool")
    if nom in membres:
        print("Vous bénéficiez d'une réduction de 5%")
    else:
        print("Aucune réduction disponible")
else:
    print("Vous ne pouvez pas éffectuer cet achat")
print("Merci & bonne journée")
