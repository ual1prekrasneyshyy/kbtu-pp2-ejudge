input_data = input()

#As my first pretest has error, I have noticed that input data can be written either in onel line or in two lines

try:
    n, x = [int(s) for s in input_data.split()]  #if input data is written in line
except Exception as e:
    n = int(input_data)   #if input data written in two lines
    x = int(input())

if 1 <= n <= pow(10, 3) and 0 <= x <= pow(10,3):
    arr = []

    for i in range(n):
        arr.insert(i, x + 2 * i)

    bitwise_xor = arr[0]

    for i in range(1, n):
        bitwise_xor ^= arr[i]

    print(bitwise_xor)
