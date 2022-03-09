import re

txt = input("Write something:\n")

x = re.sub(r'[\s,.]', ':', txt)

if x:
    print(x)
