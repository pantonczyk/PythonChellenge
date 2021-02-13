# Level 3
# http://www.pythonchallenge.com/pc/def/equality.html

file_open = open('level3.txt', 'r')
file_data = file_open.read()

data = list(file_data)

characters = []

for i in range(len(data)):
    if data[i].islower():
        if data[i + 1].isupper() and data[i + 2].isupper() and data[i + 3].isupper()\
                and data[i - 1].isupper() and data[i - 2].isupper() and data[i - 3].isupper() and data[i+4].islower()\
                and data[i-4].islower():
            characters.append(data[i])

print("".join(characters))

# Next level: http://www.pythonchallenge.com/pc/def/linkedlist.html

