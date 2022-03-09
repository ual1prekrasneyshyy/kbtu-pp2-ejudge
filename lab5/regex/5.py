import re

txt = input("Write something:\n")

x = re.findall(r"\ba.+b\b", txt)

print(x)
