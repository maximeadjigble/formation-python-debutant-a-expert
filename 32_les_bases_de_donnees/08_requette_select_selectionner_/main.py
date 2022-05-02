import sqlite3

connection = sqlite3.connect('celebrites.db')
curseur = connection.cursor()

try:
    # donnees = curseur.execute("SELECT * FROM Celebrites")
    donnees = curseur.execute("SELECT prenom, nom, age FROM Celebrites")
    # print(donnees.fetchone())
    # print(donnees.fetchall())
    for d in donnees:
        print(d)

except Exception as e:
    print(e)
finally:
    connection.close()