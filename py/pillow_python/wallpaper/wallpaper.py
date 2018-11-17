#!/usr/bin/env python3

"""
___________BY MOHAMMD ISLAM
"""

from __future__ import print_function
import os
import sys
import time
from PIL import Image, ImageDraw
import random
from termcolor import cprint


DEFAULT_WALL_WIDTH = 458
DEFAULT_WALL_HEIGHT = 813


class DrawingInImage:
    """
    This class used to draw images utalizing lines, points and polygaons
    """

    def __init__(self):
        self.arg_names = [
            'Command',
            'scree_width',
            'screen_height',
            'repetition'
        ]
        self.args = dict(zip(self.arg_names, sys.argv))
        self.width = int(sys.argv[1]) if 'scree_width' and 'screen_height' \
            in self.args.keys() else DEFAULT_WALL_WIDTH
        self.height = int(sys.argv[2]) if 'scree_width' and 'screen_height' \
            in self.args.keys() else DEFAULT_WALL_HEIGHT
        self.repetition = int(
            sys.argv[3]) if 'repetition' in self.args.keys() else 5
        self.box_width = 10
        self.box_height = 10
        self.im = Image.new('RGB',
                            (self.width, self.height),
                            color=(0, 0, 0))
        self.draw = ImageDraw.Draw(self.im)

    def drawLine(self):
        """
        Draws a line with random x and y coordinate
        """
        self.x_val = random.triangular(-5, self.width)
        self.y_val = random.triangular(-5, self.height)
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
        self.x_val = random.triangular(-5, self.width)
        self.y_val = random.triangular(-5, self.height)
        self.x2_val = self.x_val + random.randrange(self.box_width)
        self.y2_val = self.y_val + random.randrange(self.box_height)
        self.draw.point([self.x_val, self.y_val, self.x2_val, self.y2_val],
                        fill=(
            random.randrange(255),
            random.randrange(255),
            random.randrange(255)),
        )

    def drawPolygon(self):
        self.x_val = random.triangular(-5, self.width)
        self.y_val = random.triangular(-5, self.height)
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


if __name__ == '__main__':
    wall_num = 0
    putToScreen = DrawingInImage()
    for i in range(10):
        list(map(lambda x: putToScreen.drawLine(), range(1000)))
        list(map(lambda x: putToScreen.drawPolygon(), range(putToScreen.repetition)))

        wall_num += 1

        if not os.path.exists(walls_directory):
            os.makedirs(walls_directory)
        filename = os.path.join(walls_directory, f'wall{wall_num}.png')
        cprint(str(f"{wall_num:05}") + "-"*(10-len(str(wall_num))) +
               f'wall{wall_num}.png', color="blue")
        putToScreen.save(filename)

    cprint(putToScreen.args, color='grey', attrs=["bold", "dark"])
    cprint(
        f"Successfully created {wall_num} random wallpapers", on_color='on_green')
