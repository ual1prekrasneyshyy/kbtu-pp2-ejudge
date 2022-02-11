x1, y1 = [int(i) for i in input().split()]

n = int(input())

points = dict()  #dictionary

for i in range(n):
    x2, y2 = [int(j) for j in input().split()]
    points[str(i)] = ([x2, y2])

distances = dict()

for key, value in points.items():
    x2, y2 = value
    distance = pow(pow(x2-x1, 2) + pow(y2-y1, 2), 0.5)
    distances[key] = distance

distances_values = list(distances.values())

distances_values.sort()

for dv in distances_values:
    for key in distances.keys():
        if distances.get(key) == dv:  #if we found the key of distance,point
            point = points.get(key)
            x, y = point
            print(f'{x} {y}')
            break
