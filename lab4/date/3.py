import datetime as dt

now = dt.datetime.now()

print(f"Date in origin: {now}")
print(f"Date without milliseconds: {now.strftime('%Y-%m-%d %H:%M:%S')}")
