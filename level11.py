# Level 11
# http://www.pythonchallenge.com/pc/return/5808.html

# Listing 1.1 Napisz mi kurwa kod
import math
from PIL import Image

image = Image.open('cave.jpg')
(w, h) = image.size

img1 = Image.new('RGB', (math.floor(w/2), math.floor(h/2)))
img2 = Image.new('RGB', (math.floor(w/2), math.floor(h/2)))

for i in range(w):
    for j in range(h):
        pixel = image.getpixel((i, j))
        img1.putpixel((math.floor(i/2), math.floor(j/2)), pixel)

img1.show()

# Next level: http://www.pythonchallenge.com/pc/return/evil.html


