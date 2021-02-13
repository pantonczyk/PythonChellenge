# Level 16
# http://www.pythonchallenge.com/pc/return/mozart.html


from PIL import Image, ImageChops

image = Image.open("mozart.gif")

for y in range(image.size[1]):
    box = 0, y, image.size[0], y + 1
    row = image.crop(box)
    bytes = row.tobytes()
    i = bytes.index(195)
    row = ImageChops.offset(row, -i)
    image.paste(row, box)

image.show()

# 1756-01-27  brithday Mozart
# Next level: http://www.pythonchallenge.com/pc/return/romance.html
