# Level 5
# http://www.pythonchallenge.com/pc/def/peak.html

from urllib.request import urlopen
import pickle

text = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()

text1 = text.decode()

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

print(data)


for i in data:
    print("".join([a*b for a, b in i]))

# Next level: http://www.pythonchallenge.com/pc/def/channel.html

