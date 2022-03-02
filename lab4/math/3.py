#Reqular polygon - правильный многоугольник
import math
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

s = 1

if n == 3:
    s = pow(a, 2)*math.sqrt(2)/4
elif n == 4:
    s = pow(a, 2)
else:
    s = n * pow(a, 2)/(4 * math.tan( math.pi/n ) )

print(f"The area of the polygon is: {s}")
