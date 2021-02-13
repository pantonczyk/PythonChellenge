# Level 1
# http://www.pythonchallenge.com/pc/def/map.html

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result = ""

for char in text:
    if 'a' <= char <= 'z':
        result += chr(((ord(char) + 2) - ord('a')) % 26 + ord('a'))
    else:
        result += char

print(result)

# Output
"""i hope you didnt translate it by hand. thats what computers are for. doing itin by hand is inefficient and that's 
why this text is so long. using string.maketrans() is recommended. now apply on the url."""

# Maketrans
table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
result1 = text.translate(table)
print(result1)

out = "map".translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"))
print(out)

# Next level: http://www.pythonchallenge.com/pc/def/ocr.html
