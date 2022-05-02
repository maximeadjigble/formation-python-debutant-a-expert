class Achats:
    def __init__(self):
        self.produits = {}

    def ajouter(self, produit, prix):
        self.produits[produit] = prix

    def supprimer(self, produit):
        if produit in self.produits:
            del self.produits[produit]
        else:
            print("Erreur: produit invalide")

    def prix_total(self):
        total = 0
        # for p in self.produits:
        #    total += self.produits[p]
        for p, v in self.produits.items():
            total += v
        
        print("Prix total:", total, "euros")

    def afficher(self):
        print("----------------")
        for i, p in enumerate(self.produits):
            print(f"{i} : {p} - {self.produits[p]} euros")

achats = Achats()

achats.ajouter("banane", 3.6)
achats.ajouter("oeuf", 2.5)
achats.ajouter("salade", 3)

while True:
    cmd = input("Commandes (+: Ajouter, s: Supprimer, t: Afficher le prix total, a: Afficher, q: Quitter) ")

    if cmd == "+":
        produit = input("Entrez le produit: ")
        prix = float(input("Entrez le prix: "))
        achats.ajouter(produit, prix)
    elif cmd == "s":
        produit = input("Entrez le produit: ")
        achats.supprimer(produit)
    elif cmd == "t":
        achats.prix_total()
    elif cmd == "a":
        achats.afficher()
    elif cmd == "q":
        break
    else:
        print("Commande invalide")







# achats.afficher()
# achats.prix_total()

# achats.afficher()
# achats.supprimer("oeuf")
# achats.afficher()
