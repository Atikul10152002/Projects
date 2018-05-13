from PIL import Image, ImageDraw
from random import randrange, triangular, choice

# Can be many different formats.
imag = Image.open('/Users/atikul/Downloads/626201613142.png')
pix = imag.load()
print(imag.size)

im = Image.new('RGB',
               (imag.size[0], imag.size[1]),
               color=(0, 0, 0))
draw = ImageDraw.Draw(im)


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


def filter_im(filtername):
    # print(args)
    global imag, pix
    list(map(lambda y: list(map(lambda x: draw.point([x, y], fill=(
        filtername(pix[x, y]))), range(imag.size[1]))),  range(imag.size[0])))
    imag = im
    pix = imag.load()
    print(str(filtername), "Complete")


filter_im(inverse_pixalate_color)
# filter_im(blacknwhite)
# filter_im(blue_filter)
# filter_im(red_filter)
# filter_im(green_filter)
# filter_im(blacknwhite)

im.save("wall.png")
im.show()
