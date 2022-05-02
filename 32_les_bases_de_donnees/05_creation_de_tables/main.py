import sqlite3

connection = sqlite3.connect('celebrites.db')
curseur = connection.cursor()

try:
    curseur.execute('''CREATE TABLE IF NOT EXISTS Celebrites 
                    (id INT PRIMARY KEY,
                    nom TEXT,
                    prenom TEXT,
                    age INTEGER,
                    popularite REAL)''')
except Exception as e:
    print(e)
finally:
    connection.close()