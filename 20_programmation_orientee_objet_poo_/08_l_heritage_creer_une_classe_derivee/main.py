class Personne():
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher_infos(self):
        print(f"Infos: {self.nom} {self.prenom} {self.age}")

class Etudiant(Personne):
    pass

romeo = Personne("Santos", "Romeo", 39)
alicia = Etudiant("Keys", "Alicia", 39)
romeo.afficher_infos()
alicia.afficher_infos()

