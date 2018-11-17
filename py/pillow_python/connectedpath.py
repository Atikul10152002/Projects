from PIL import Image, ImageDraw
from random import sample, choice, randint
from termcolor import cprint
import colorama
colorama.init()


IMAGEWIDTH = 500
IMAGEHEIGHT = 500
ellipse_width = 1
line_width = 1
num_point = 1000
reps = 1


save_file_ = 'wall.png'


im = Image.new('RGB', (IMAGEWIDTH,IMAGEHEIGHT))
draw = ImageDraw.Draw(im)

points = [sample(range(round(sum([IMAGEWIDTH,IMAGEHEIGHT])/2)), 2) for _ in range(num_point)]

for _ in range(reps):
    ex, ey = choice(points)
    for _ in range(len(points)):
        x, y = choice(points)
        draw.line([ex,ey,x,y], fill=(255,255,255), width=line_width)
        # draw.line([ex,ey,x,y], fill=(randint(0,255),randint(0,255),randint(0,255)), width=line_width)
        draw.ellipse((x-ellipse_width, y-ellipse_width, x+ellipse_width, y+ellipse_width), 'blue')
        # points.remove([x,y]) 
        # ex, ey = x, y
    # print(points)
    draw.ellipse((ex-ellipse_width, ey-ellipse_width, ex+ellipse_width, ey+ellipse_width), 'green')

im.save(save_file_)
cprint("Image saved as " + save_file_, color="green")