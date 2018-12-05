import math
import time
from random import randint
from PIL import Image, ImageDraw, ImageFilter
save_file_ = 'output.png'


class Circles:
    """Circles("626201613142.png")"""

    def __init__(self, filename):
        self.filename = filename
        self.image = self.im = Image.open(str(filename))
        self.im = self.image.filter(ImageFilter.GaussianBlur(radius=10))
        self.pix = self.im.load()
        self.size = self.im.size
        self.line_wid: int = 1
        self.circle_radius_factor = 30
        self.division = 3
        self.blank_image = self.image
        # self.blank_image = Image.new(
        # 'RGB', (self.size[0], self.size[1]), color=(0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)
        print('circle_radius_factor : ', self.circle_radius_factor)
        print('size : ', self.size)

        self.circle_lining()
        self.blank_image.save(save_file_)

    def __repr__(self): return f"Cools({self.filename})"

    def circle_lining(self):
        list_start_time = time.time()

        list(map(lambda width:
                 list(map(lambda height:
                          self.draw.ellipse(
                            [
                              round(
                                  width * self.division - round(sum(self.pix[width * self.division, height * self.division])/self.circle_radius_factor) * math.cos(randint(0, 360))),
                              round(
                                  height * self.division - round(sum(self.pix[width * self.division, height * self.division])/self.circle_radius_factor) * math.cos(randint(0, 360))),
                              round(
                                  width * self.division+round(sum(self.pix[width * self.division, height * self.division])/self.circle_radius_factor) * math.cos(randint(0, 360))),
                              round(
                                  height * self.division+round(sum(self.pix[width * self.division, height * self.division])/self.circle_radius_factor) * math.cos(randint(0, 360)))
                            ],
                              outline=self.pix[width * self.division, height * self.division],
                              fill=self.pix[width * self.division, height * self.division]),
                          range(self.size[1]//self.division))),
                 range(self.size[0]//self.division)))

        print('List Comprehension finished in', time.time()-list_start_time)


Circles('input.png')
