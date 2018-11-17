import sys
import time
from random import choice, triangular
from PIL import Image


class Filter_image():
    """
    Filter_imag("626201613142.png")
    """

    def __init__(self, filename):
        self.filename = filename
        self.imag =  self.im = Image.open(str(filename))
        self.pix = self.imag.load()
        self.size = self.imag.size
        self._width = self.size[0]
        self._height = self.size[1]
        # self.im = Image.new("RGB",self.size)

    def __repr__(self):
        return f"Filter_imag({self.filename})"

    def __str__(self):
        return f"\nFilter_imag(\"{self.filename}\")\n\filter(\
        [\"inverse_pix\", \"blacknwhite\", \"inverse_pix\"], \
        x=0, y=0, width=200, height=400)\n"

    def filter(self, filtername, x=0, y=0, width=0, height=0, show_filtered_img=False):
        start_time = time.time()
        self.x = x
        self.y = y
        self.width = width if width != 0 else self.size[0]
        self.height = height if height != 0 else self.size[1]
        self.filtername = filtername
        print(self.size[0]*self.size[1], "Pixels\n")
        # self.im.pixels[100,100] = (255,255,255)

        # massive list and maps
        list_start_time = time.time()

        print("Processing")
        list(map(lambda _filter: self.im.putdata([(self.filterdict[_filter](self.pix[x_cord, y_cord]))for y_cord in range(round(self.y), min(
                self.size[1], round(self.y+self.height))) for x_cord in range(round(self.x), min(self.size[0], round(self.x+self.width)))]), self.filtername))
        
        # for _filter in self.filtername:
        #     _filter_time = time.time()
        #     print(self.filterdict[_filter].__name__, "Processing")

            # pixels_arr = [(self.filterdict[_filter](self.pix[x_cord, y_cord]))for y_cord in range(round(self.y), min(
            #     self.size[1], round(self.y+self.height))) for x_cord in range(round(self.x), min(self.size[0], round(self.x+self.width)))]
            
            # self.im.putdata([(self.filterdict[_filter](self.pix[x_cord, y_cord]))for y_cord in range(round(self.y), min(
            #     self.size[1], round(self.y+self.height))) for x_cord in range(round(self.x), min(self.size[0], round(self.x+self.width)))])

        print("list comprehension finished in", time.time()-list_start_time )

        self.save()
        if show_filtered_img == True:
            self.show()
        print(str(filtername), "Complete in", time.time()-start_time)
        # print(self.imag.size)

    @staticmethod
    def inverse_color(pix):
        red = 255-pix[0]
        green = 255-pix[1]
        blue = 255-pix[2]
        # return (green, blue, red)
        return (red, green, blue)

    @staticmethod
    def inverse_pixalate_color(pix):
        red = round(triangular(-1, pix[0]))
        green = round(triangular(-1, pix[1]))
        blue = round(triangular(-1, pix[2]))
        return (choice([(0, 0, 0), (red, green, blue)]))

    # brighter -->
    # def inverse_pixalate_color(pix):
    #     red = round(triangular(pix[0], 255))
    #     green = round(triangular(pix[1], 255))
    #     blue = round(triangular(pix[2], 255))
    #     return (choice([(0, 0, 0), (red, green, blue)]))

    @staticmethod
    def blue_filter(pix):
        red = 255-pix[0]
        green = 255-pix[1]
        blue = 0
        return (red, green, blue)

    @staticmethod
    def red_filter(pix):
        red = 0
        green = 255-pix[1]
        blue = 255-pix[2]
        return (red, green, blue)

    @staticmethod
    def green_filter(pix):
        red = 255-pix[0]
        green = 0
        blue = 255-pix[2]
        return (red, green, blue)

    @staticmethod
    def blacknwhite(pix):
        average = (pix[0]+pix[1]+pix[2])/3
        red = round(average)
        green = round(average)
        blue = round(average)
        return (red, green, blue)

    def show(self):
        self.im.show()

    def save(self):
        self.im.save("wall.png")


"""
'inverse',
'inverse_pix',
'blue',
'red',
'green',
'blacknwhite'
"""


def sample():
    filter_im = Filter_image(
        "20180224_173418.jpg")

    # filter_im.show()

    filter_im.filter(
        ["blacknwhite"], 0, 0,
        filter_im.size[0], filter_im.size[1])


if __name__ == "__main__":
    sample()
