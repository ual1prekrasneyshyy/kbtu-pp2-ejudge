binary_number = input()  #input data

def convert_bite_to_number(index = 0):  #default value for local variable index is 0. It is also begging value
    global binary_number
    if index == len(binary_number)-1:
        return int(binary_number[index])
    return int(binary_number[index])*pow(2, len(binary_number)-index-1)+convert_bite_to_number(index+1)  #iterating value of index

if 1 <= len(binary_number) <= 30:  #check the length of input data
    decimal_number = convert_bite_to_number()  #get decimal number from recursion
    print(decimal_number)
