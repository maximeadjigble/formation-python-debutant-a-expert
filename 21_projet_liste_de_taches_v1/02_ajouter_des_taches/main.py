class Taches:
    def __init__(self):
        self.taches = []
        self.termine = []

    def ajouter(self, tache):
        self.taches.append(tache)
        self.termine.append(False)

taches = Taches()

taches.ajouter("Aller au supermarché")
taches.ajouter("Appeler Clément")
taches.ajouter("Néttoyer la voiture")


print(taches.taches)
print(taches.termine)