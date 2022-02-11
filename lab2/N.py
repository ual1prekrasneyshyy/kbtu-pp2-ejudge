# import numpy as np #I import this library to create vector.
#
#HOW CAN I USE VECTOR, IF EJUDGE SYSTEM THROWS MODULE NOT FOUND ERROR!
input_list = []

while True:   #i don't exactly know how many entries will be
    input_number = int(input())
    if input_number == 0:   #If entry is zero, the inputing of data stops
        break
    input_list.append(input_number)

vector1 = []  #i need to split whole list in two lists by pairs
vector2 = []

quantity_of_entries = len(input_list)

for i in range(int(quantity_of_entries/2)): #If quantity of numbers if even, for example 4, then i=0,1, if odd, 5 for example, i=0,1. function int() will round 5/2=2,5=2
    vector1.insert(i, input_list[i])  #first, second, third,... elements from beginning
    vector2.insert(i, input_list[-1-i]) #paired first, second, third,... elemnts from the end

if quantity_of_entries % 2 != 0:   #If quanity of numbers is odd, the middle entry will not be included by the previous block code
    vector1.append(input_list[int(quantity_of_entries/2)])
    vector2.append(0)  #because lengths of two vectors should be equal.

# vector1 = np.array(vector1)    #convert lists to vector
# vector2 = np.array(vector2)

# pairs = vector1 + vector2     #adding paired numbers as adding coordinates of vector,

# I don't know why ejudge tells me "ModuleNotFoundError: No module named 'numpy'"  I will solve by using alternative way

pairs = []

for i in range(len(vector1)): #lengths of vector1 and vector2 equal
    pairs.insert(i, vector1[i]+vector2[i])   #It like in vector v=(x1+x2, y1+y2, z1+z2, ...)

output_data = "" #if I write print(pairs), the result will be [x y z ...] as coordinates of vector, but here answer should be without btackets

for paired_value in pairs:
    output_data += f'{paired_value} '

print(output_data)



