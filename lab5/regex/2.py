import re

s = input("Write something:\n")

x = re.findall(r"abbb?", s)

print(x)
