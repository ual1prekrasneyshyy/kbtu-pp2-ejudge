n = int(input())
if 1 <= n <= pow(10,5):
    demons = {} #it is dictionary, key=weakness, value=number of demons with such weakness. We are not interested in demons' names
    for i in range(n):
        d, w = input().split()
        if not demons.keys().__contains__(w):
            demons[w] = 1
        else:
            demons.update({w: demons[w]+1})

    m = int(input())
    if 1 <= m <= pow(10,5):
        hunters = {}   #key=ability, value=approximate number of demons that can be killed
        for i in range(m):
            h,a,k = input().split()
            if not hunters.keys().__contains__(a):
                hunters[a] = int(k)
            else:
                hunters.update({a: hunters[a] + int(k)})

        for a in hunters.keys(): #abilities
            if demons.keys().__contains__(a): #ability of hunter = weakness of demon
                if demons[a] > hunters[a]:  #we compare number of all demons with such weakness and the possible number of demons that can be killed by hunter with such ability
                    n -= hunters[a]
                else:
                    n -= demons[a]


        print(f'Demons left: {n}')
