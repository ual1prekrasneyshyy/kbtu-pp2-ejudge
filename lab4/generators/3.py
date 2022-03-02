def gen_3_4_(n):
    i = 0

    while i <= n:
        if i % 3 == 0 or i % 4 == 0:
            yield i
        i += 1

n = int(input("Insert some number:\n"))

for i in gen_3_4_(n):
    print(i)
