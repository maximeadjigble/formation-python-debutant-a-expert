prenom = "Maxime"

def salutation():
    global prenom
    prenom = "Sylvie"
    print("Bonjour", prenom)

print("Avant", prenom)
salutation()
print("Après", prenom)
print("Fin")