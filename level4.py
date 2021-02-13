# Level 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import re
from urllib.request import urlopen

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

#numer = "12345"
numer = str(16044/2)

tmp = re.compile("and the next nothing is (\d+)")

while True:
    tmp1 = urlopen(url % numer).read().decode('utf-8')
    print(tmp1)
    match = tmp.search(tmp1)
    if match is None:
        break
    numer = match.group(1)


# Next level: http://www.pythonchallenge.com/pc/def/peak.html

