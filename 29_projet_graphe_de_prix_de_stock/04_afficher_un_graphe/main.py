import turtle

donnees = [2,5,4,6,2,4,8,2,3,5,9,2,4,2,1,4,5,6,4,8]

turtle.getscreen()

#Initialiser la position du curseur
s = turtle.screensize()
offset_x = -s[0] + 50
turtle.up()
turtle.setpos(offset_x,0)
turtle.down()

for i, v in enumerate(donnees):
    x = i*10 + offset_x
    y = v*20
    turtle.goto(x, y)

turtle.done()