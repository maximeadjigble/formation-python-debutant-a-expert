class Taches:
    def __init__(self):
        self.taches = []
        self.termine = []

    def ajouter(self, tache):
        self.taches.append(tache)
        self.termine.append(False)

    def afficher(self):
        print('--------------------')
        for i, t in enumerate(self.taches):
            print(f'{i} : {t} - {self.termine[i]}')


taches = Taches()

taches.ajouter("Aller au supermarché")
taches.ajouter("Appeler Clément")
taches.ajouter("Néttoyer la voiture")


taches.afficher()
# print(taches.taches)
# print(taches.termine)