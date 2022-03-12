import re

txt = input("Write something:\n")

x = re.findall(r"^a.+b$", txt)

print(x)
