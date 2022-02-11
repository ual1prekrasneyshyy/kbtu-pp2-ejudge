arr = [int(a) for a in input().split() if 0 <= int(a) <= pow(10,4)]
n = len(arr)

#We will check the possibility to get the largest element from the end of array
possibilities = [0 for i in range(n-1)]  #here i=0 means the possiblity to reach from the zero's element, i=1, from the first.
possibilities.append(1)  #i=(n-1)-th should be one. Because we don't need to jump from last element to last.

for i in range(n-2, -1, -1): #We start checking the probability to reach the end of array from the pre-last element (предпоследний), after we move to the previous element
    if arr[i] >= possibilities.index(1)-i:   #We use operator >= because the value of arr[i] means, that jump can be done not just through arr[i] positions, arr[i] is max, and the number of positions, through which jump can be done, is in interval [1,arr(i)]       #in the probability array, all check and verified positions denoted by 1. We need to work with the first one, which has already been analyzed.
        possibilities[i] = 1 # We mark that index as possible due to fact, after we check the probability to reach from previus elemts to current, denoted by i, not last

print(possibilities[0])  # It means, that we analyzed and marked, that it is either possible or not to reach the last element, starting from the begging