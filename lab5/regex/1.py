import re

s = input("Write something:\n")

x = re.findall(r'ab*', s)

print(x)


