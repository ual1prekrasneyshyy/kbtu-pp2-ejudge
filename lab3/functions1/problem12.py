def histogram(arr):
    for i in arr:
        print('*'*i)


li = list(map(int, input("Write some numbers separated by space for histogram\n").split()))

histogram(li)
