import re

txt = input("Write something:\n")

x = re.findall('[a-z]+', txt)

print(x)
