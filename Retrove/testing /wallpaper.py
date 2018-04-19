#!/usr/bin/env python3

"""
"""

from __future__ import print_function
import os
import sys
import time
from PIL import Image, ImageDraw
import random


DEFAULT_WALL_WIDTH = 1200
DEFAULT_WALL_HEIGHT = 800

# try:
arg_names = ['Command', 'scree_width', 'screen_height', 'repetition']
args = dict(zip(arg_names, sys.argv))
print(args)

width = int(sys.argv[1]) if 'scree_width' and 'screen_height' in args.keys(
) else DEFAULT_WALL_WIDTH
height = int(sys.argv[2]) if 'scree_width' and 'screen_height' in args.keys(
) else DEFAULT_WALL_HEIGHT
repetition = int(sys.argv[3]) if 'repetition' in args.keys() else 20

# except Exception as e:
#     if os.name != 'nt':
#         os.system('clear')
#     else:
#         os.system('cls')
#     print(
#         """\nUsage:\n\npython wallpaper.py [options]\n[options] = \n\n""",
#         """     \'repetition of polygons\', \'scree_width\', \'screen_height\'\n""",
#         """        <all options should be integers>\n\n""",
#         """         Ex. python wallpaper.py 100 400 800""")


class DrawingInImage:
    def __init__(self):
        self.box_width = 10
        self.box_height = 10
        self.im = Image.new('RGB',
                            (width, height),
                            color=(0, 0, 0))
        self.draw = ImageDraw.Draw(self.im)

    def drawLine(self):
        self.x_val = random.triangular(-5, width)
        self.y_val = random.triangular(-5, height)
        self.x2_val = self.x_val + random.randrange(self.box_width)
        self.y2_val = self.y_val + random.randrange(self.box_height)
        self.draw.line([self.x_val, self.y_val, self.x2_val, self.y2_val],
                       fill=(
            random.randrange(255),
            random.randrange(255),
            random.randrange(255)),
            width=1
        )

    def drawPoint(self):
        self.x_val = random.triangular(-5, width)
        self.y_val = random.triangular(-5, height)
        self.x2_val = self.x_val + random.randrange(self.box_width)
        self.y2_val = self.y_val + random.randrange(self.box_height)
        self.draw.point([self.x_val, self.y_val, self.x2_val, self.y2_val],
                        fill=(
            random.randrange(255),
            random.randrange(255),
            random.randrange(255)),
        )

    def drawPolygon(self):
        self.x_val = random.triangular(-5, width)
        self.y_val = random.triangular(-5, height)
        self.x2_val = self.x_val + random.randrange(self.box_width)
        self.y2_val = self.y_val + random.randrange(self.box_height)
        self.draw.polygon(
            [
                random.choice([self.x_val, -self.x_val]),
                random.choice([self.y_val, -self.y_val]),
                random.choice([self.x2_val, -self.x2_val]),
                random.choice([self.y2_val, -self.y2_val]),
                random.choice([-self.y_val*2, self.y_val*2]),
                random.choice([-self.x_val*2]),
                random.choice([-self.y_val//2, self.y_val*2]),
                random.choice([-self.x_val//2])
            ],
            fill=(
                round(random.randrange(0, 200)),
                round(random.randrange(0, 255)),
                round(random.randrange(0, 255))
            ))

    def save(self, filename):
        self.im.save(filename)


current_wd = os.path.dirname(os.path.realpath(sys.argv[0]))
walls_directory = os.path.join(current_wd, "walls")


wall_num = 0
for i in range(10):
    # while 1:
    putToScreen = DrawingInImage()
    list(map(lambda x: putToScreen.drawLine(), range(1000)))
    list(map(lambda x: putToScreen.drawPolygon(), range(repetition)))

    wall_num += 1

    if not os.path.exists(walls_directory):
        os.makedirs(walls_directory)
    filename = os.path.join(walls_directory, 'wall{}.png'.format(wall_num))
    print(wall_num, "-->", filename, os.getcwd())
    putToScreen.save(filename)

# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
