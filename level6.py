# Level 6
# http://www.pythonchallenge.com/pc/def/channel.html

import zipfile
import re

file = zipfile.ZipFile("channel.zip")
numer = "90052"

comments = []

while True:
    content = file.read(numer + ".txt").decode('utf-8')
    print(content)
    comments.append(file.getinfo(numer + ".txt").comment.decode('utf-8'))
    match = re.search("Next nothing is (\d+)", content)
    if match is None:
        break
    numer = match.group(1)

print("".join(comments))


# Next level: http://www.pythonchallenge.com/pc/def/oxygen.html

