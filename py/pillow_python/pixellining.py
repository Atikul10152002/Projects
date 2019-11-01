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

        self.line_len_factor: int = round(self.size[0]*.002)
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

        print("List Comprehension finished in",
              (time.time()-list_start_time))
        self.finishing_touch()
        self.blank_image.save(save_file_)

    def __repr__(self):
        return f"Cools({self.filename})"

    def finishing_touch(self):
        data = list(self.blank_image.getdata())
        for w in range(len(data)):
            if w < len(data)-10 and w > 10 and sum(data[w]) < 5:
                for i in range(10):
                    if sum(data[w+i]) > 5:
                        data[w] = data[w+i]
                        break
                    elif sum(data[w-i]) > 5:
                        data[w] = data[w-i]
                        break
                    else:
                        continue
        self.blank_image.putdata(data)


llk = Cools("output.png")
