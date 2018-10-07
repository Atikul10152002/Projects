import turtle as d
from cairosvg import svg2png
import canvasvg

d.shape("turtle")
d.screensize(2000, 1500)
d.speed(0)
d.pu()
d.goto(x=0,y=-100)
d.pd()

angle = 0
increase = 1
while 1:
    
    d.circle(200)
    d.left(increase)
    angle += increase
    print(angle)
    if angle >= 360:
        break


d.hideturtle()
canv = d.getscreen().getcanvas()
canvasvg.saveall("turtle.svg", canv)
exit()
d.done()
