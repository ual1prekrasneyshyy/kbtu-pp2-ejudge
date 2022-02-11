import datetime    #I Additional knowledge

dates = []

while True:
    date = input() #dd mm yyyy
    if date == "0":
        break
    dd, mm, yyyy = [int(i) for i in date.split()]
    dates.append(datetime.datetime(yyyy, mm, dd))

dates.sort()

for date in dates:
    dd = date.day
    mm = date.month
    yyyy = date.year

    if dd < 10:   #formating date
        dd = f'0{dd}'
    if mm < 10:
        mm = f'0{mm}'
    if yyyy < 10:
        yyyy = f'000{yyyy}'
    elif yyyy < 100:
        yyyy = f'00{yyyy}'
    elif yyyy < 1000:
        yyyy = f'0{yyyy}'
    print(f'{dd} {mm} {yyyy}')
