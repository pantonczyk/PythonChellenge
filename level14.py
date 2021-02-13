# Level 14
# http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image

image = Image.open('wire.png')
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
out = Image.new('RGB', [100, 100])
x, y, p = -1, 0, 0
d = 200
while d / 2 > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y), image.getpixel((p, 0)))
            p += 1
        d -= 1
out.show()
# Next level: http://www.pythonchallenge.com/pc/return/cat.html
# http://www.pythonchallenge.com/pc/return/uzi.html
