def gen(n: int):
    while n >= 0:
        yield n
        n -= 1


n = int(input("n="))
for g in gen(n):
    print(g)
