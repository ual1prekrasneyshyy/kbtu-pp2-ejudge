s = input()

def count_ascii_sum(index):
    global s

    if(index>0):
        return ord(s[index])+count_ascii_sum(index-1)
    else:
        return ord(s[index])


if count_ascii_sum(len(s)-1) > 300:
    print("It is tasty!")
else:
    print("Oh, no!")
