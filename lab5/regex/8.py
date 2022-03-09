import re

s = input("Write something:\n")

x = re.findall("[A-Z][a-z]*", s)

print(x)
