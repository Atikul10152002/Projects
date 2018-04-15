#!/usr/bin/env python3

"""
Wall creator by Mohammad
"""

import os
import sys
import time
import pip
pip.main(['install', "pillow"])
from PIL import Image, ImageDraw
import random


DEFAULT_WALL_WIDTH = 400
DEFAULT_WALL_HEIGHT = 800

try:
    arg_names = ['Command', 'repetition', 'scree_width', 'screen_height']
    args = dict(zip(arg_names, sys.argv))
    # print(args)

    repetition = int(sys.argv[1]) if 'repetition' in args.keys() else 20
    width = int(sys.argv[2]) if 'scree_width' and 'screen_height' in args.keys(
    ) else DEFAULT_WALL_WIDTH
    height = int(sys.argv[3]) if 'scree_width' and 'screen_height' in args.keys(
    ) else DEFAULT_WALL_HEIGHT

except Exception as e:
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')
    print(
        """\nUsage:\n\npython wallpaper.py [options]\n[options] = \n\n""",
        """     \'repetition of polygons\', \'scree_width\', \'screen_height\'\n""",
        """        <all options should be integers>\n\n""",
        """         Ex. python wallpaper.py 100 400 800""")

try:
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

    wall_num = 0
    for i in range(10):
        putToScreen = DrawingInImage()
        list(map(lambda x: putToScreen.drawLine(), range(1000)))
        list(map(lambda x: putToScreen.drawPolygon(), range(repetition)))

        wall_num += 1
        if not os.path.exists("walls"):
            os.makedirs("walls")
        filename = 'walls/wall{}.png'.format(wall_num)
        print(wall_num)
        putToScreen.save(filename)
        # time.sleep(.1)
except Exception as e:
    print("\n\nError <", e, "")
