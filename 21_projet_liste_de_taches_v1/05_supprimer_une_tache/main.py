class Taches:
    def __init__(self):
        self.taches = []
        self.termine = []

    def ajouter(self, tache):
        self.taches.append(tache)
        self.termine.append(False)

    def idx_valid(self, idx):
        if idx >= 0 and idx < len(self.taches):
            return True
        else:
            print("Erreur: Indice hors limites")
            return False

    def terminer(self, idx):
        if self.idx_valid(idx):
            self.termine[idx] = True

    def supprimer(self, idx):
        if self.idx_valid(idx):
            del self.taches[idx]
            del self.termine[idx]

    def afficher(self):
        print('--------------------')
        for i, t in enumerate(self.taches):
            print(f'{i} : {t} - {self.termine[i]}')


taches = Taches()

taches.ajouter("Aller au supermarché")
taches.ajouter("Appeler Clément")
taches.ajouter("Néttoyer la voiture")

taches.afficher()
taches.terminer(1)
taches.afficher()
taches.supprimer(1)
taches.afficher()
# print(taches.taches)
# print(taches.termine)