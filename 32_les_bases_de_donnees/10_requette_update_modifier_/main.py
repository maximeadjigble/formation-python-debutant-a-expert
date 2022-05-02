import sqlite3

connection = sqlite3.connect('celebrites.db')
curseur = connection.cursor()

try:
    donnees = curseur.execute("""SELECT * FROM Celebrites
                            WHERE nom='Berry'""")
    print("Avant",donnees.fetchone())

    curseur.execute("""UPDATE Celebrites 
                SET age=54, popularite = 8.5
                WHERE nom='Berry'""")
    connection.commit()

    donnees = curseur.execute("""SELECT * FROM Celebrites
                            WHERE nom='Berry'""")
    print("Apres", donnees.fetchone())





except Exception as e:
    print(e)
finally:
    connection.close()