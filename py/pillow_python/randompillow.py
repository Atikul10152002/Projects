import sys
import time
from random import choice
from PIL import Image, ImageDraw

save_file_ = "upward.png"

class Cools():
    """
    Filter_imag("626201613142.png")
    """

    def __init__(self, filename):
        self.filename = filename
        self.imag = self.im = Image.open(str(filename)) 
        self.draw = ImageDraw.Draw(self.imag)
        self.pix = self.imag.load()
        self.size = self.imag.size
        self._width = self.size[0]
        self._height = self.size[1]
        self.line_len = 5

        list(map(lambda wid: list(map(lambda hei: 
            self. draw.line([wid, hei, wid + choice([self.line_len, -self.line_len]), hei + choice([self.line_len, -self.line_len])], fill=self.pix[wid, hei], width=1), \
            range(self._height))), range(self._width)))

        # for wid in range(self._width):
        #     for hei in range(self._height):
        #         self. draw.line([wid, hei, wid + choice([self.line_len,   -self.line_len]), hei + choice([self.line_len, -self.line_len])],fill=self.pix[wid, hei], width=1)
        self.imag.save(save_file_)

    def __repr__(self):
        return f"Filter_imag({self.filename})"


llk = Cools("face.jpg")



