from PIL import Image, ImageDraw
from random import randint, choice
from pyprogressbar import prg

IMAGEWITH = 500
IMAGEHEIGHT = 500
line_len = 5
line_width = 1
num_line = 50

save_file_ = 'wall.png'

im = Image.new('RGB', (IMAGEWITH,IMAGEHEIGHT))
draw = ImageDraw.Draw(im)


x_end = y_end = 0
iteration =  0
for i in range(num_line):
    x = ex = 0
    y = ey = 0
    prg(i,num_line)
    while 1:
        # x+= randint(0,line_len)
        # y+= randint(0,line_len)
        x+= choice([0,line_len])
        y+= choice([0,line_len])
        # y-= choice([0,line_len])

        draw.line([ex,ey,x,y], fill=(255,255,255), width=line_width) 
        ex, ey = x,y
        if x >= im.width or y >= im.height:
            x_end+=x; y_end+=y; iteration+=1
            break
        
# draw.line([0,0,round((x_end/iteration)+10),round((y_end/iteration)+10)], fill=255,width=2)
im.save(save_file_)
print("Image saved as ",save_file_)
