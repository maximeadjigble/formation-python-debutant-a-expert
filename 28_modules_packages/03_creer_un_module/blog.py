class Utilisateur():
    def __init__(self,prenom, nom,  age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
 
    def info(self, label = ''):
        print(f"{label} {self.prenom} {self.nom} {self.age}")
 
    def ajouter(self):
        print(f"{self.prenom} {self.nom} ajouté à la base de données")
 
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