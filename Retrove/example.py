from PIL import Image, ImageDraw
import random
import sys
import time
import os

try:
    repetition = int(sys.argv[1])
except:
    repetition = 100

width = 455
height = 809
box_width = 10
box_height = 10
wall_num = 0

for i in range(10):
    im = Image.new('RGB', (width, height), color=(0, 0, 0))
    # im.putdata(mylist)
    draw = ImageDraw.Draw(im)

    for i in range(1000):
        x_val = random.triangular(-5, width)
        y_val = random.triangular(-5, height)
        x2_val = x_val + random.randrange(box_width)
        y2_val = y_val + random.randrange(box_height)
        draw.line([x_val, y_val, x2_val, y2_val],
                  fill=(random.randrange(255), random.randrange(255), random.randrange(255)), width=1)
    for i in range(repetition):
        x_val = random.triangular(-5, width)
        y_val = random.triangular(-5, height)
        x2_val = x_val + random.randrange(box_width)
        y2_val = y_val + random.randrange(box_height)
        draw.polygon([random.choice([x_val, -x_val]), random.choice([y_val, -y_val]), random.choice([x2_val, -x2_val]), random.choice([y2_val, -y2_val]), random.choice([-y_val*2, y_val*2]), random.choice(
            [-x_val*2]), random.choice([-y_val//2, y_val*2]), random.choice([-x_val//2])], fill=(round(random.randrange(0, 200)), round(random.randrange(0, 255)), round(random.randrange(0, 255))))
    wall_num += 1
    if not os.path.exists("walls"):
        os.makedirs("walls")
    filename = 'walls/wall{}.png'.format(wall_num)
    print(wall_num)
    im.save(filename)
    # time.sleep(.1)
