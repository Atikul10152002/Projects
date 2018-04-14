from PIL import Image
import random

mylist = []

for i in range((40*40)):
    color = (random.randrange(255), random.randrange(
        255), random.randrange(255))
    mylist.append(color)

img = Image.new('RGB', (40, 40))
img.putdata(mylist)
img.save('wall.png')
