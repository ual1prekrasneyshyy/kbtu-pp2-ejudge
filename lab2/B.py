n = int(input())
if 2 <= n <= 500:  #because 2<=n<=500
    a = [int(s) for s in input().split() if 1 <= int(s) <= 100]  #because 1<=Ai<=500 of all elements of array
    a.sort(reverse=True)  #I sort in reverse order
    print(a[0]*a[1])  #As the order is reversed, the largest element is first, the second largest element is the second element
