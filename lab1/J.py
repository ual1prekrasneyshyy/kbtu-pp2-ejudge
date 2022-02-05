s = input()
s = s.split(" ")
new_string = ""

for s1 in s:  #s1 is separate word
    if(len(s1)>=3):
        new_string+=s1+" "

print(new_string)