def is_palendrom(s: str) -> bool:
    for i in range(int(len(s)/2)):
        if s[i] != s[-1-i]:
            return False

    return True


s1 = input("Write a string:\n")

if is_palendrom(s1):
    print(f'{s1} is palendrom')
else:
    print(f'{s1} is not palendrom')
