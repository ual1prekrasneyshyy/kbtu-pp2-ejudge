my_array = [int(a) for a in input().split() if 0 <= int(a) <= pow(10,4)]
my_array_length = len(my_array)

if 1 <= my_array_length <= pow(10,3):
    current_index = 0

    while current_index < my_array_length:
        if my_array[current_index + my_array[current_index]] != 0:
            current_index += my_array[current_index]
        else:
            current_index += my_array[current_index]-1
            