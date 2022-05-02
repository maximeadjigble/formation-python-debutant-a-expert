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

    def existe(self, tache):
        requette = f"SELECT * FROM Taches WHERE tache = '{tache}'"
        resultat = self.curseur.execute(requette).fetchone()
        return True if resultat else False

    def ajouter(self, tache, etat=False):
        requette = f"INSERT INTO Taches (tache, etat) VALUES ('{tache}',{int(etat)})"
        # print(requette)
        self.curseur.execute(requette)
        self.connection.commit()

    def afficher(self):
        requette = "SELECT * FROM Taches"
        # print(requette)
        taches = self.curseur.execute(requette).fetchall()
        print('-----------------')
        for t in taches:
            if t[2]:
                print(f"{t[0]} - {barrer(t[1])}")
            else:
                print(f"{t[0]} - {t[1]}")

    def recuperer(self):
        requette = "SELECT * FROM Taches"
        return self.curseur.execute(requette).fetchall()

    def terminer(self, tache):
        if self.existe(tache):
            requette = f"UPDATE Taches SET etat = 1 WHERE tache = '{tache}'"
            self.curseur.execute(requette)
            self.connection.commit()
            print(f"{tache} terminée")
        else:
            print("La tache n'existe pas...")

    def supprimer(self, tache):
        requette = f"DELETE FROM Taches WHERE tache = '{tache}'"
        self.curseur.execute(requette)
        self.connection.commit()

# id: 15, tache: 'Aller au Marché', etat: 0/1
taches = Taches()

try:
    taches.db_connecter()
    taches.afficher()
    
    # taches.supprimer("Aller au parc")
    # taches.afficher()
    # taches.terminer("Aller au supermarché")
    # taches.afficher()
    # taches.ajouter("Aller au parc", True)
    # # taches.ajouter("Aller au supermarché")
    # taches.ajouter("Appeler Clément")
    # taches.ajouter("Néttoyer la voiture")
except Exception as e:
    print("Erreur", e)
finally: 
    taches.db_fermer()












