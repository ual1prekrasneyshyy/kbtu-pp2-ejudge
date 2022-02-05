array = [int(a) for a in input().split() if 0 <= int(a) <= pow(10, 4)]

array_length = len(array)

if 1 <= array_length <= pow(10, 3):
    current_index = 0
    for i in range(array_length):
        if i != current_index:
            continue
        current_index += array[current_index]

        if current_index+1 >= array_length:
            print(1)
            break
