import sqlite3

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


# id: 15
# tache: 'Aller au Marché' 
# etat: 0/1
taches = Taches()














