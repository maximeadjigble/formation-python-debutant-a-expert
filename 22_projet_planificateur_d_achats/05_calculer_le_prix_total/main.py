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

achats.afficher()
achats.prix_total()

# achats.afficher()
# achats.supprimer("oeuf")
# achats.afficher()
