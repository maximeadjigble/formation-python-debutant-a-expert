class Rectangle:
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur

    def perimetre(self):
        print("Périmètre:",2*(self.longeur + self.largeur) , "m")

    def aire(self):
        print("Aire:", self.longeur*self.largeur , "m^2")

    def est_carre(self):
        print("Est carré?:", self.longeur == self.largeur)

rect = Rectangle(10, 10)
rect.perimetre()
rect.aire()
rect.est_carre()