# Level 10
# http://www.pythonchallenge.com/pc/return/bull.html

# a = [1, 11, 21, 1211, 111221, 312211, 13112221 ........... ]

def seq(a):
    a = str(a)
    count = 1
    last = a[0]
    result = ''
    for i in range(1, len(a)):  # przechodzimy po całym wyrazie
        if last == a[i]:  # jeżeli ostatni znak jest identyczny jak napotkany zwiększ licznik
            count += 1
        else:  # jeżeji nie, to dodaj licznik i liczbę do wyniku
            result = result + str(count) + last
            count = 1
        last = a[i]
    result = result + str(count) + last
    return result


i = 0
a = 1
while i < 30:
    a = seq(a)
    print(len(a))
    i += 1


# Next level: http://www.pythonchallenge.com/pc/return/5808.html
