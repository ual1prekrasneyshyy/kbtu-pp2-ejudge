n = int(input())

if 1 <= n <= pow(10, 5):
    students_data = dict()

    for i in range(n):
        surname, compensation = input().split()
        compensation = int(compensation)
        if 1 <= len(surname) <= 100 and 1 <= compensation <= pow(10, 4):
            if surname in students_data.keys():
                students_data.update({ surname : students_data.get(surname)+compensation })
            else:
                students_data[surname] = compensation

    list_of_compensations = list(students_data.values()).copy()
    list_of_compensations.sort(reverse=True)
    max_compensation = list_of_compensations[0]



    list_of_surnames = list(students_data.keys())
    list_of_surnames.sort()

    for surname in list_of_surnames:
        compensation = students_data[surname]
        if compensation==max_compensation:
            print(f'{surname} is lucky!')
        else:
            difference_of_compensation = max_compensation - compensation
            print(f'{surname} has to receive {difference_of_compensation} tenge')