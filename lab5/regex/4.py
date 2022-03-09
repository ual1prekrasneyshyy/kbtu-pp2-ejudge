import re

txt = input("Write something:\n")

x = re.findall("[A-Z][a-z]*", txt)

print(x)
