n = int(input())

if n % 2 != 0:  #if n is odd
    for i in range(n):
        row_to_print = ""
        for j in range(n-1-i):
            row_to_print += "."
        for j in range(i+1):
            row_to_print += "#"
        print(row_to_print)
else:
    for i in range(n):
        row_to_print = ""
        for j in range(i + 1):
            row_to_print += "#"
        for j in range(n-1-i):
            row_to_print += "."
        print(row_to_print)
