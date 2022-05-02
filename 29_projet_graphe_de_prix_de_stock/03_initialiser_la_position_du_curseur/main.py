import turtle

turtle.getscreen()

s = turtle.screensize()
offset_x = -s[0] + 50
turtle.up()
turtle.setpos(offset_x,0)
turtle.down()

turtle.done()