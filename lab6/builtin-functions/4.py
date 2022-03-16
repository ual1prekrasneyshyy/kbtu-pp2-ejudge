import time

n = int(input('Insert number n:\n'))
ms = int(input('Insert time of delay in milliseconds:\n'))

time.sleep(ms/1000)

print(f'The square root of {n} after {ms} milliseconds is {pow(n, 0.5)}')

