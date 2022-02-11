n = int(input())

passwords = []

if 1 <= n <= pow(n,3):

    for i in range(n):
        passwords.append(input())

    strong_passwords = set()  #save unique

    for password in passwords:
        contains_upper = False
        contains_lower = False
        contains_number = False

        for char in password:
            if 48 <= ord(char) <= 57:
                contains_number = True
            elif 65 <= ord(char) <= 90:
                contains_upper = True
            elif 97 <= ord(char) <= 122:
                contains_lower = True

        if contains_upper and contains_lower and contains_number:
            strong_passwords.add(password)

    strong_passwords = list(strong_passwords)
    strong_passwords.sort() #it should be sorted

    print(len(strong_passwords))
    for p in strong_passwords:
        print(p)