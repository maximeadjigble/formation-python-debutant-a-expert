import sqlite3

connection = sqlite3.connect('celebrites.db')
curseur = connection.cursor()

try:
    # donnees = curseur.execute("SELECT * FROM Celebrites")
    # donnees = curseur.execute("""SELECT * FROM Celebrites
    #                         WHERE nom='Cruise'""")

    # donnees = curseur.execute("""SELECT * FROM Celebrites
    #                     WHERE popularite <= 8.5""")

    # donnees = curseur.execute("""SELECT * FROM Celebrites
    #                     ORDER BY -popularite""")

    donnees = curseur.execute("""SELECT * FROM Celebrites
                        WHERE popularite < 8.7
                        ORDER BY -popularite""")
    # print(donnees.fetchone())
    # print(donnees.fetchall())
    for d in donnees:
        print(d)

except Exception as e:
    print(e)
finally:
    connection.close()