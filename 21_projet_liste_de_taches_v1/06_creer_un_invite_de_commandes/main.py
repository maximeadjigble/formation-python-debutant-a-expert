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

while True:
    cmd = input("Entrez une commande (+: Ajouter, -: Terminer, s: Supprimer, a: Afficher, q: Quitter) ")

    if cmd == "+":
        tache = input("Entrez le nom: ")
        taches.ajouter(tache)
    elif cmd == "-":
        idx = int(input("Entrez l'id de la tâche: "))
        taches.terminer(idx)
    elif cmd == "s":
        idx = int(input("Entrez l'id de la tâche: "))
        taches.supprimer(idx)
    elif cmd == "a":
        taches.afficher()
    elif cmd == "q":
        break
    else:
        print("Commande invalide")


# taches.afficher()
# taches.terminer(1)
# taches.afficher()
# taches.supprimer(1)
# taches.afficher()


