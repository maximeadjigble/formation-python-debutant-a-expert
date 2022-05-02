import sqlite3

connection = sqlite3.connect('celebrites.db')
curseur = connection.cursor()

try:
    # curseur.execute('''CREATE TABLE IF NOT EXISTS Celebrites (id INT PRIMARY KEY, nom TEXT, prenom TEXT, age INTEGER, popularite REAL)''')
    # curseur.execute('''INSERT INTO Celebrites
    #                 (id, prenom, nom, age, popularite) 
    #                 VALUES
    #                 (1, "Tom", "Cruise", 58, 8.2)''')
    curseur.execute('''INSERT INTO Celebrites
                    (id, prenom, nom, age, popularite) 
                    VALUES
                    (2, "Halle", "Berry", 54, 8.5)''')
    curseur.execute('''INSERT INTO Celebrites
                    (id, prenom, nom, age, popularite) 
                    VALUES
                    (3, "Dwayne", "Johnson", 48, 9.1)''')
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()