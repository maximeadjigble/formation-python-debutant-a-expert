class Achats:
    def __init__(self):
        self.produits = {}

    def ajouter(self, produit, prix):
        self.produits[produit] = prix

achats = Achats()

achats.ajouter("banane", 3.6)
achats.ajouter("oeuf", 2.5)
achats.ajouter("salade", 3)
print(achats.produits)
