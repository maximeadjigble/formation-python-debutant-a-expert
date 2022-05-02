import turtle
import csv


#Echelle d'affichage
echelle_x = 2000
echelle_y = 70
zoom = 0.001
N_affichage = 40

donnees = []

#Chargement du fichier CSV
with open('AMZN.csv') as f:
    lecteur = csv.reader(f)

    next(lecteur, None)
    for ligne in lecteur:
        # print(ligne)
        d = float(ligne[1])
        donnees.append(d)

    # for i, ligne in enumerate(lecteur):
    #     if i != 0:
    #         print(ligne)

turtle.getscreen()

#Personalisation
turtle.title("Stock AMZN")
turtle.speed(6)
turtle.color("black", "black")


#Initialiser la position du curseur
s = turtle.screensize()
offset_x = -s[0] + 50

#Afficher l'axe X
turtle.up()
turtle.setpos(-s[0], 0)
turtle.down()
turtle.setpos(2*s[0], 0)

#Afficher l'axe Y
turtle.up()
turtle.setpos(offset_x, -s[1])
turtle.down()
turtle.setpos(offset_x, 2*s[1])


turtle.color("red", "black")
turtle.up()
turtle.setpos(offset_x,0)
turtle.down()

#Afficher les valeurs sur le graphe
for i, v in enumerate(donnees):
    x = zoom*i*echelle_x + offset_x
    y = zoom*v*echelle_y

    #Positioner le curseur sur l'axe Y
    if i == 0:
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
    else:
        turtle.goto(x, y)

    #Afficher les valeurs sur le graphe
    if i % N_affichage == 0:
        turtle.color("green", "black")
        turtle.write(int(v), font=("Verdana", 12, "bold"))
        turtle.dot(5)
        turtle.color("red", "black")


turtle.done()