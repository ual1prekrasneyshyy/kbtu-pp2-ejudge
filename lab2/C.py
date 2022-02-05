n = int(input())
# if 1 <= n <= 99:
#I comment the range limit 1<=n<=99 because I had wrong answer on the 100th pretest, where n was equal to 100.
multiplication_table = []
for y in range(n): #y=0,1,2,...,n
    row = []
    for x in range(n): #start filling the row; x=0,1,2,...,n
        cell = 0  #the default value is 0
        if y == 0:
            cell = x  #iterating first row to n
        elif x == 0:
            cell = y #iterating first column to n
        elif x == y:
            cell = x * y #diagonal is result of multiplication
        row.insert(x, cell)  #add x-th cell to the row
    multiplication_table.insert(y, row) #add y-th row to the table

for row in multiplication_table:
    string_value_of_row_of_matrix = ""     #prepare to print row
    for cell in row:
        string_value_of_row_of_matrix += str(cell) + " "    #add every cell to the string which will be printed
    print(string_value_of_row_of_matrix)  #print row
