def squares(a: int, b: int):
    while a <= b:
        yield pow(a, 2)
        a += 1


a = int(input("a="))
b = int(input("b="))

for s in squares(a,b):
    print(s)
