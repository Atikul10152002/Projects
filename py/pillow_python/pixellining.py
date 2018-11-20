import time
from random import randint
from PIL import Image, ImageDraw
import math

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

        self.line_len_factor: int = round(self.size[0]*.009)
        self.line_wid: int = 2

        # self.blank_image = self.image
        self.blank_image = Image.new('RGB', (self.size[0], self.size[1]))

        self.draw = ImageDraw.Draw(self.blank_image)

        print("line_len_factor : ", self.line_len_factor)
        print("line_wid : ", self.line_wid)
        print("size : ", self.size)

        list_start_time: float = time.time()

        list(
            map(
                lambda width:
                list(
                    map(lambda height:

                        self. draw.line(
                            [width,
                             height,
                             round(
                                 width + round(sum(self.pix[width, height])/self.line_len_factor) * math.cos(randint(0, 360))),
                             round(
                                 height + round(sum(self.pix[width, height])/self.line_len_factor) * math.sin(randint(0, 360)))],

                            fill=self.pix[width, height],
                            width=self.line_wid
                        ),
                        range(self.size[1])
                        )
                ),
                range(self.size[0])
            )
        )

        print("List Comprehension finished in", str(
            (time.time()-list_start_time)/60)[:4], " minutes")

        self.blank_image.save(save_file_)

    def __repr__(self):
        return f"Cools({self.filename})"


llk = Cools("wallpaper/walls/wall9.png")
# llk = Cools("input.png")
