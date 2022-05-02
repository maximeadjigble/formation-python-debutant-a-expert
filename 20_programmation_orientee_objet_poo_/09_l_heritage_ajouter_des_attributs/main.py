class Personne():
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher_infos(self):
        print(f"Infos: {self.nom} {self.prenom} {self.age}")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, notes):
        # Personne.__init__(self, nom, prenom, age)
        super().__init__(nom, prenom, age)
        self.notes = notes

romeo = Personne("Santos", "Romeo", 39)
alicia = Etudiant("Keys", "Alicia", 39, {"mathématiques": 14, "physique": 13.5, "lv1": 16})

romeo.afficher_infos()
alicia.afficher_infos()
print(alicia.notes)
# print(romeo.notes)

