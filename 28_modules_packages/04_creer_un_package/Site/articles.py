class Article():
    def __init__(self, titre, contenu, auteur=None):
        self.titre = titre
        self.contenu = contenu
        self.auteur = auteur
 
    def modifier(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
 
    def afficher(self):
        print("> Article ")
        print("Titre:", self.titre)
        print("Contenu:", self.contenu)
        if self.auteur:
            self.auteur.info('Auteur:')