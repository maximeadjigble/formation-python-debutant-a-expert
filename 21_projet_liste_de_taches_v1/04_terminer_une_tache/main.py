class Taches:
    def __init__(self):
        self.taches = []
        self.termine = []

    def ajouter(self, tache):
        self.taches.append(tache)
        self.termine.append(False)

    def terminer(self, idx):
        if idx >= 0 and idx < len(self.termine):
            self.termine[idx] = True
        else:
            print("Erreur: Indice hors limites")

    def afficher(self):
        print('--------------------')
        for i, t in enumerate(self.taches):
            print(f'{i} : {t} - {self.termine[i]}')


taches = Taches()

taches.ajouter("Aller au supermarché")
taches.ajouter("Appeler Clément")
taches.ajouter("Néttoyer la voiture")

taches.afficher()
taches.terminer(2)
taches.afficher()
# print(taches.taches)
# print(taches.termine)