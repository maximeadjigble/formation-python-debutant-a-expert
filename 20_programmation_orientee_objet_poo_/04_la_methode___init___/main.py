class Personne: 
    def __init__(self, nom, prenom, age):
        self.nom = nom 
        self.prenom = prenom 
        self.age = age

bruce = Personne("Willis", "Bruce", 38)
alice = Personne("Eve", "Alice", 38)

print(bruce.nom, bruce.prenom, bruce.age)
print(alice.nom, alice.prenom, alice.age)
# print(Personne.nom, Personne.prenom, Personne.age)