# Level 2
# http://www.pythonchallenge.com/pc/def/ocr.html

import urllib.request
import re
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
data = open('level2.txt').read()
print("".join(re.findall("[A-Za-z]", data)))

# Next level: http://www.pythonchallenge.com/pc/def/equality.html

