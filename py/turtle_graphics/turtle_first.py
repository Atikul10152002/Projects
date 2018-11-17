import turtle
import canvasvg
import math

d = turtle.Turtle()
d.shape("turtle")
# turtle.screensize(2000, 1500)
d.speed(0)
d.pu()
d.goto(-100,50)
d.pd()
d.color("red")

def star(obj, size):
    if size < 10:
        return
    for i in range(5):
        obj.fd(size)
        star(obj, size /3)
        obj.lt(216)

star(d,200)
d.pu()
d.goto(0,0)
d.left(90)
d.pd()
# d.hideturtle()
canv = d.getscreen().getcanvas()
canvasvg.saveall("turtle.svg", canv)
turtle.done()
