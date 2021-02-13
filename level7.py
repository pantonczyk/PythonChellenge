# Level 7
# http://www.pythonchallenge.com/pc/def/oxygen.html
# pip install pypng

from urllib.request import urlopen
import png, re

picture = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")

(w, h, rgba, dummy) = png.Reader(picture).read()

color = list(rgba)
mid = int(h / 2)
length = len(color[mid])
res = [chr(color[mid][i]) for i in range(0, length, 4*7) if color[mid][i] == color[mid][i + 1] == color[mid][i + 2]]

print("".join(res))
print("".join(map(chr, map(int, re.findall("\d+", "".join(res))))))

# Next level: http://www.pythonchallenge.com/pc/def/integrity.html

