# Level 12
# http://www.pythonchallenge.com/pc/return/evil.html

# C:\Users\pablo>curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg
# Bert is evil! go back!

file = open('evil2.gfx', 'rb').read()
print(file)

print(len(file))

for i in range(5):
    open('%d.jpg' % i, 'wb').write(file[i::5])

# Next level: http://www.pythonchallenge.com/pc/return/disproportional.html


