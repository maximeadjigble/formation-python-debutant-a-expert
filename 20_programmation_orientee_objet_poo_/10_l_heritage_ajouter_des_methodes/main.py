class Personne():
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher_infos(self):
        print(f"Infos: {self.nom} {self.prenom} {self.age}")

    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, notes):
        super().__init__(nom, prenom, age)
        self.notes = notes

    def ajouter_note(self, matiere, note):
        self.notes[matiere] = note

    def afficher_moyenne(self):
        moyenne = list(self.notes.values())
        moyenne = sum(moyenne)/float(len(moyenne))
        print(f"La moyenne de {self.nom_complet()} est {moyenne}")


class Musicien(Personne):
    def __init__(self, nom, prenom, age, instrument):
        super().__init__(nom, prenom, age)
        self.instrument = instrument


romeo = Musicien("Santos", "Romeo", 39, "flutte")
alicia = Etudiant("Keys", "Alicia", 39, {"mathématiques": 14, "physique": 13.5, "lv1": 16})

print(romeo.instrument)
print(alicia.notes)


# alicia.ajouter_note("lv2", 11)
# alicia.afficher_moyenne()

# romeo.afficher_infos()
# alicia.afficher_infos()
# print(alicia.notes)

