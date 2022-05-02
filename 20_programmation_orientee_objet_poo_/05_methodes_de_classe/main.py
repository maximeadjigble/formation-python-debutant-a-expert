class Personne: 
    def __init__(self, nom, prenom, age):
        self.nom = nom 
        self.prenom = prenom 
        self.age = age
        self.email = None

    def afficher_infos(self):
        print(f"Infos: {self.nom} {self.prenom} {self.age} {self.email}")

    def changer_email(self, email):
        self.email = email
        return self.email

bruce = Personne("Willis", "Bruce", 38)
alice = Personne("Eve", "Alice", 38)

email = bruce.changer_email("bruce.willis@gmail.com")
print(email)

bruce.afficher_infos()
alice.afficher_infos()

# print("Infos:", bruce.nom, bruce.prenom, bruce.age)
# print("Infos:", alice.nom, alice.prenom, alice.age)