import turtle
import canvasvg

d = turtle.Turtle()
d.shape("turtle")
d.speed(0)
d.pu()
d.goto(x=0,y=-100)
d.pd()

angle = 0
while 1:
    d.circle(200)
    d.left(1)
    angle += 1
    if angle >= 360:
        break

d.hideturtle()
canv = d.getscreen().getcanvas()
canvasvg.saveall("turtle.svg", canv)

turtle.done()
