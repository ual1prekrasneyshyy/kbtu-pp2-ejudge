import re

s = input("Write something:\n")

words = re.findall("[A-Z][a-z]*", s)

s1 = ""
for w in words:
    s1 += w + " "

print(s1)
