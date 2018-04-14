from PIL import Image, ImageDraw


class create_image():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new(
            "RGB", (self.width, self.height), (200, 200, 200))
        self.size = self.image.size

    def repetition(self, colors, rect):
        self.image.paste(self.colors, self.rect)

    def save(self):
        self.image.save("wall.png")


new_im = create_image(40, 40)

new_im.repetition((55, 44, 200), [0, 0, new_im.size[0]/10, new_im.size[1]/10])
