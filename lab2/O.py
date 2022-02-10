digits_encodings = {        #It is like database, which contains all string values of every digits, where key - string, value - int
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOU": 4,
    "FIV": 5,
    "SIX": 6,
    "SEV": 7,
    "EIG": 8,
    "NIN": 9,
    "ZER": 0
}


def convert_string_number_to_integer(string_value_of_number):   #This fuction converts string value of number to integer
    global digits_encodings
    digits_quantity = int(len(string_value_of_number) / 3)   #because string value of every digit contains three characters
    int_value = 0   #initial value
    for i in range(1, digits_quantity + 1):  # i=1,2,3,.....,n
        #Example: 235 = 100*2+10*3+1*5=2*10^(3-1)+3*10^(3-2)+5*10^(3-3), there are 3 digigts in the number
        int_value += pow(10, digits_quantity - i) * digits_encodings[string_value_of_number[(3 * i - 3):(3 * i)]] #it is splitting one whole string to substrings of length 3 #0:3 (from 0 to 2), 3:6 (from 3 to 5), 6:9 (from 6 to 8)
    return int_value


def convert_int_to_string(int_value):  #this function converts integer to its string value
    global digits_encodings
    inverse_list_of_string_values_of_digits = [] #I will get digits from the end of number
    while int_value > 0:
        digit = int_value % 10    # n-th digit, (n-1)-th digit, (n-2)-th digit, ...., where n is number of digits
        int_value = (int_value - digit) / 10   # it will delete last digit
        for key in digits_encodings.keys():   #i need to find the key of value
            if digits_encodings.get(key) == digit:
                inverse_list_of_string_values_of_digits.append(key)
                break

    string_value_of_number = ""   #initial value
    inverse_list_of_string_values_of_digits.reverse()   #because order was reversed
    for string_value_of_digit in inverse_list_of_string_values_of_digits:
        string_value_of_number += string_value_of_digit   #append every string value digit to the string value value of number
    return string_value_of_number


summands = input().split("+")  # summand - слагаемое  #It like two number a,b. I need to find a+b
int_sum = convert_string_number_to_integer(summands[0]) + convert_string_number_to_integer(summands[1])   #get integer values and find sum
print(convert_int_to_string(int_sum)) #print the result in a string form
