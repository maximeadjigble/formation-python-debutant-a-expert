import sqlite3

def barrer(texte):
    return ''.join([u'\u0336{}'.format(c) for c in texte])

class Taches:
    def __init__(self):
        self.db_nom = 'taches.db'
        self.db_connecter()
        self.curseur.execute('''CREATE TABLE IF NOT EXISTS Taches
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        tache TEXTE, etat INTEGER)''')
        self.db_fermer()

    def db_connecter(self):
        self.connection = sqlite3.connect(self.db_nom)
        self.curseur = self.connection.cursor()

    def db_fermer(self):
        self.connection.close()

    def ajouter(self, tache, etat=False):
        self.db_connecter()
        requette = f"INSERT INTO Taches (tache, etat) VALUES ('{tache}',{int(etat)})"
        print(requette)
        self.curseur.execute(requette)
        self.connection.commit()
        self.db_fermer()

    def afficher(self):
        self.db_connecter()
        requette = "SELECT * FROM Taches"
        print(requette)
        taches = self.curseur.execute(requette).fetchall()
        for t in taches:
            if t[2]:
                print(f"{t[0]} - {barrer(t[1])}, {t[2]}")
            else:
                print(f"{t[0]} - {t[1]}, {t[2]}")
        self.db_fermer()




# id: 15
# tache: 'Aller au Marché' 
# etat: 0/1
taches = Taches()

try:
    taches.ajouter("Aller au parc", True)
    taches.afficher()

    # # taches.ajouter("Aller au supermarché")
    # taches.ajouter("Appeler Clément")
    # taches.ajouter("Néttoyer la voiture")
except Exception as e:
    print("Erreur", e)
finally: 
    taches.db_fermer()












