def is_prime(x):
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            return 0
    return 1


filter = lambda a: is_prime(a)


n = int(input("Write some number\nn="))
prime = filter(n)

if prime > 0:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")
