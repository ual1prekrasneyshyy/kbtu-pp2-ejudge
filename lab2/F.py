n = int(input())

if 1 <= n <= pow(10, 5):
    students_data = dict()

    for i in range(n):
        surname, compensation = input().split()  #one property is string, other - integer
        compensation = int(compensation)  #because this property should be integer
        if 1 <= len(surname) <= 100 and 1 <= compensation <= pow(10, 4):
            if surname in students_data.keys():  #who knows, perhaps student with this surname already has received compesation, he or she exists in the dictionary
                students_data.update({ surname : students_data.get(surname)+compensation })  #I sum already recieved sum and sum which is going to be received
            else:
                students_data[surname] = compensation

    list_of_compensations = list(students_data.values()).copy()  #I get all compensation
    list_of_compensations.sort(reverse=True) #I sort list in descending order to make easier finding maximum
    max_compensation = list_of_compensations[0]  #Maximum is first element because order is descending

    #As a have understood, I should write the students in ascending order by students surname

    list_of_surnames = list(students_data.keys())
    list_of_surnames.sort()

    for surname in list_of_surnames:
        compensation = students_data[surname]
        if compensation==max_compensation:
            print(f'{surname} is lucky!')
        else:
            difference_of_compensation = max_compensation - compensation
            print(f'{surname} has to receive {difference_of_compensation} tenge')