import sqlite3

connection = sqlite3.connect('celebrites.db')
curseur = connection.cursor()

try:
    #Créer la table
    curseur.execute('''CREATE TABLE IF NOT EXISTS Celebrites 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, 
                age INTEGER, popularite REAL)''')
    
    #Ajouter des célébrités
    curseur.execute('''INSERT INTO Celebrites
                    (prenom, nom, age, popularite) 
                    VALUES
                    ("Tom", "Cruise", 58, 8.2)''')
    curseur.execute('''INSERT INTO Celebrites
                    (prenom, nom, age, popularite) 
                    VALUES
                    ("Halle", "Berry", 54, 8.5)''')
    curseur.execute('''INSERT INTO Celebrites
                    (prenom, nom, age, popularite) 
                    VALUES
                    ("Dwayne", "Johnson", 48, 9.1)''')
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()