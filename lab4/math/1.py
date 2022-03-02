import math

degree = float(input("Input degree: "))

if degree > 360:
    degree = degree % 360

radian = degree * math.pi / 180

print('Output radian: %.6f' % radian)
