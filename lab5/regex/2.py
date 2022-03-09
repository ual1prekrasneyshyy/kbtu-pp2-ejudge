import re

s = input("Write something:\n")

x = re.findall("abbb?", s)

print(x)
