import math
import time
from random import randint
from PIL import Image, ImageDraw

save_file_: str = "upward.png"


class Cools():
    """
    Filter_imag("626201613142.png")
    """

    def __init__(self, filename):

        self.filename = filename
        self.image = self.im = Image.open(str(filename))
        self.pix = self.image.load()
        self.size = self.image.size

        self.circle_radius_factor: int = 50

        #self.blank_image = self.image
        self.blank_image = Image.new('RGB', (self.size[0], self.size[1]))

        self.draw = ImageDraw.Draw(self.blank_image)

        print("cricle_radius_factor : ", self.circle_radius_factor)
        print("size : ", self.size)

        list_start_time: float = time.time()

        list(map(lambda width:
                 list(map(lambda height:
                          self.draw.ellipse([
                              round(
                                  width - round(sum(self.pix[width, height])/self.circle_radius_factor) * math.cos(randint(0, 360))),
                              round(
                                  height - round(sum(self.pix[width, height])/self.circle_radius_factor) * math.cos(randint(0, 360))),
                              round(
                                  width+round(sum(self.pix[width, height])/self.circle_radius_factor) * math.cos(randint(0, 360))),
                              round(
                                  height+round(sum(self.pix[width, height])/self.circle_radius_factor) * math.cos(randint(0, 360)))
                          ]
                          ,outline=self.pix[width, height],fill=None),
                          range(self.size[1]))),
                 range(self.size[0])))

        print("List Comprehension finished in",
              (time.time()-list_start_time))

        self.blank_image.save(save_file_)

    def __repr__(self):
        return f"Cools({self.filename})"


llk=Cools("input.jpg")
