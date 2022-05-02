class Achats:
    def __init__(self):
        self.produits = {}

    def ajouter(self, produit, prix):
        self.produits[produit] = prix

    def afficher(self):
        print("----------------")
        for i, p in enumerate(self.produits):
            print(f"{i} : {p} - {self.produits[p]} euros")

achats = Achats()

achats.ajouter("banane", 3.6)
achats.ajouter("oeuf", 2.5)
achats.ajouter("salade", 3)

achats.afficher()
