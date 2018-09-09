from PIL import Image, ImageDraw
import sys

img = Image.open(sys.argv[1])
img = img.convert("RGBA")
datas = img.getdata()
newData = []
threashhodld = 50
for item in datas:
    if item[0] >= threashhodld and item[1] >= threashhodld and item[2] >= threashhodld:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)


img.putdata(newData)
img.show()
img.save('test.png', 'PNG')
