n = int(input())
arr = []

if 0 <= n <= 100:
    for i in range(n):
        a = int(input())
        if 0 <= a <= 168:
            arr.append(a)
    for a in arr:
        if a <= 10:
            print("Go to work!")
        elif 10 < a <= 25:
            print("You are weak")
        elif 25 < a <= 45:
            print("Okay, fine")
        elif a > 45:
            print("Burn! Burn! Burn Young!")