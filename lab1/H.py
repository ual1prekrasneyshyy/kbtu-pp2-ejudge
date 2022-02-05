s = input()
t = input()

if 1 <= len(s) <= 100 and len(t) == 1:
    indexes_of_occurring = []

    for i in range(len(s)):
        if(s[i]==t):
            indexes_of_occurring.append(i)


    if(len(indexes_of_occurring)==1):
        print(indexes_of_occurring[0])
    elif(len(indexes_of_occurring)>1):
        print(f'{indexes_of_occurring[0]} {indexes_of_occurring[-1]}')