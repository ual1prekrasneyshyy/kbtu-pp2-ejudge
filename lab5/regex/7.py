import re

txt = input("Write in snake case:\n")

subtxt = re.split(r'_', txt)

txt1 = ''

for j in range(len(subtxt)):
    s = subtxt[j]
    for i in range(len(s)):
        if i == 0 and j > 0:  #Camel Case. First letter is in lower case
            txt1 += s[i].upper()
        else:
            txt1 += s[i]

# txt1.replace(txt1[0], txt1[0].lower())
print("Camel case: ")
print(txt1)
