n = int(input())

if 1 <= n <= 100:
    given_discs = []
    taken_disks = []
    index = 0
    for i in range(n):
        operation = input()
        if operation != "2":
            given_discs.append(operation.split(" ")[1])
        else:
            taken_disks.append(given_discs[index])
            index += 1

    print_answer = ""

    for d in taken_disks:
        print_answer += d + " "

    print(print_answer)