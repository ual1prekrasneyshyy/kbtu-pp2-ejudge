import datetime as dat

today = dat.datetime.now()
yesterday = today + dat.timedelta(days=-1)
tomorrow = today + dat.timedelta(days=1)

print(f"Yesterday was {yesterday.strftime('%d/%m/%Y')}")
print(f"Today is {today.strftime('%d/%m/%Y')}")
print(f"Tomorrow will be {tomorrow.strftime('%d/%m/%Y')}")
