import re

txt = input("Write something:\n")

x = re.finditer('_?(?P<word>[a-z]+)_?', txt)

for w in x:
    print(w.group('word'))
