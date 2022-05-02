import turtle

donnees = [2,5,4,6,2,4,8,2,3,5,9,2,4,2,1,4,5,6,4,8]

turtle.getscreen()

#Personalisation
turtle.title("Stock AMZN")
turtle.speed(6)
turtle.color("red", "black")


#Initialiser la position du curseur
s = turtle.screensize()
offset_x = -s[0] + 50
turtle.up()
turtle.setpos(offset_x,0)
turtle.down()

#Echelle d'affichage
echelle_x = 10
echelle_y = 20
zoom = 1

#Afficher les valeurs sur le graphe
for i, v in enumerate(donnees):
    x = zoom*i*echelle_x + offset_x
    y = zoom*v*echelle_y
    turtle.goto(x, y)

turtle.done()