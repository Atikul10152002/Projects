import math
import time
from random import randint
from PIL import Image, ImageDraw, ImageFilter
save_file_ = 'output.png'


class Circles:
    """Circles("626201613142.png")"""

    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(str(filename))
        self.im = self.image.filter(ImageFilter.GaussianBlur(radius=10))
        self.pix = self.im.load()
        self.size = self.im.size
        self.circle_radius_factor = 50
        self.blank_image = Image.new(
            'RGB', (self.size[0], self.size[1]), color=(0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.blank_image)
        print('circle_radius_factor : ', self.circle_radius_factor)
        print('size : ', self.size)
        self.circle_lining(reps=1)
        self.finishing_touch()
        self.blank_image.save(save_file_)

    def __repr__(self): return f"Cools({self.filename})"

    def circle_lining(self, reps):
        list_start_time = time.time()

        list(map(lambda _: list(map(lambda width: list(map(lambda height: self.draw.ellipse([round(width-round(sum(self.pix[(width, height)])/self.circle_radius_factor)*math.cos(randint(0, 360))), round(height-round(sum(self.pix[(width, height)])/self.circle_radius_factor)*math.cos(randint(0, 360))), round(
            width+round(sum(self.pix[(width, height)])/self.circle_radius_factor)*math.cos(randint(0, 360))), round(height+round(sum(self.pix[(width, height)])/self.circle_radius_factor)*math.cos(randint(0, 360)))], outline=self.pix[(width, height)], fill=None), range(self.size[1]))), range(self.size[0]))), range(reps)))

        print('List Comprehension finished in', time.time()-list_start_time)

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


Circles('input.png')
