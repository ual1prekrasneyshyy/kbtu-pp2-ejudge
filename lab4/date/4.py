import datetime as dt

# arr = list(map(int, input("Insert data in format: years months days hours minutes seconds\n").split()))
# d1 = dt.datetime(year=arr[0], month=arr[1], day=arr[2], hour=arr[3], minute=arr[4], second=arr[5])
# arr = list(map(int, input("Insert data in format: years months days hours minutes seconds\n").split()))
# d2 = dt.datetime(year=arr[0], month=arr[1], day=arr[2], hour=arr[3], minute=arr[4], second=arr[5])


date_1 = dt.datetime(year=2020, month=6, day=5) #Settable, Changable
date_2 = dt.datetime(year=2012, month=1, day=3)

ds = (date_2-date_1).total_seconds()
ds = int(ds)
ds = abs(ds)

print(f"ds={ds}")


