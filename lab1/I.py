n = int(input())

if 1 <= n <= 100:
    possible_emails = []
    for i in range(n):
        s = input()
        possible_emails.append(s)

    for possible_email in possible_emails:
        if "@gmail.com" in possible_email:
            print(possible_email.split("@")[0])