import sqlite3

connection = sqlite3.connect('celebrites.db')
curseur = connection.cursor()

try:
    donnees = curseur.execute("""SELECT * FROM Celebrites""")
    print("Avant ==========")
    for d in donnees:
        print(d)

    curseur.execute("""DELETE FROM Celebrites
                    WHERE popularite < 6""")
    connection.commit()

    donnees = curseur.execute("""SELECT * FROM Celebrites""")
    print("Apres ==========")
    for d in donnees:
        print(d)





except Exception as e:
    print(e)
finally:
    connection.close()