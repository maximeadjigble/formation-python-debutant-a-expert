class Utilisateur():
    def __init__(self,prenom, nom,  age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
 
    def info(self, label = ''):
        print(f"{label} {self.prenom} {self.nom} {self.age}")
 
    def ajouter(self):
        print(f"{self.prenom} {self.nom} ajouté à la base de données")
 