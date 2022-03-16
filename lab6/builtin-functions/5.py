def is_all_items_true(arr: tuple) -> bool:
    return all(arr)


tuple_1 = (True, True, True)
tuple_2 = (True, False, True)
tuple_3 = (True, 34, 67.5, "Hello", 'a')
tuple_4 = (False, 1, {}, "", {'': ''})

tuples = (tuple_1, tuple_2, tuple_3, tuple_4)

for i in range(len(tuples)):
    print(f'{i+1} - {is_all_items_true(tuples[i])}')
