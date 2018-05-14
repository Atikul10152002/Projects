from PIL import Image
from random import randrange, triangular, choice

imag = im = Image.open('/Users/atikul/Downloads/626201613142.png')
pix = imag.load()
print(imag.size)

_imag_width = imag.size[0]
_imag_height = imag.size[1]


# im = imag
# draw = ImageDraw.Draw(im)

# class Filter_image():
#     def __self__(filename, filtername):

def inverse_color(pix):
    red = 255-pix[0]
    green = 255-pix[1]
    blue = 255-pix[2]
    # return (green, blue, red)
    return (red, green, blue)

def inverse_pixalate_color(pix):
    red = round(triangular(-1, pix[0]))
    green = round(triangular(-1, pix[1]))
    blue = round(triangular(-1, pix[2]))
    return (choice([(0, 0, 0), (red, green, blue)]))


def blue_filter(pix):
    red = 255-pix[0]
    green = 255-pix[1]
    blue = 0
    return (red, green, blue)


def red_filter(pix):
    red = 0
    green = 255-pix[1]
    blue = 255-pix[2]
    return (red, green, blue)

def green_filter(pix):
    red = 255-pix[0]
    green = 0
    blue = 255-pix[2]
    return (red, green, blue)

def blacknwhite(pix):
    average = (pix[0]+pix[0]+pix[0])/3
    red = round(average)
    green = round(average)
    blue = round(average)
    return (red, green, blue)


def Hllp(var):
    im[var[0], var[1]] = var


def filter_im(filtername, x=0, y=0, width=_imag_width, height=_imag_height):
    """
    """
    list(map(lambda y_cord: list(map(lambda x_cord: 
        im.putpixel((x_cord, y_cord), (filtername(pix[x_cord, y_cord]))),
        range(round(x),round(x+width)))), range(round(y),round(y+height))))
    # imag = im
    # pix = imag.load()
    print(str(filtername.__name__), "Complete")


filter_im(inverse_color, _imag_width/2, _imag_height/2, 200,200)
# filter_im(blacknwhite)
# filter_im(blue_filter)
# filter_im(red_filter)
# filter_im(green_filter)
# filter_im(blacknwhite)

im.save("wall.png")
im.show()
