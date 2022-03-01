import datetime as dt

# now = dt.datetime.now()

# day = now.day
# month = now.month
# year = now.year
#
# if day > 5:
#     day -= 5
# else: #if day <= 5, then we go to the previous month
#     if month > 1:
#         month -= 1
#     else:
#         year -= 1
#         month = month + 12 - 1
#
#     days_of_previous_month = 31
#
#     if month == 4 or month == 6 or month == 9 or month == 11:
#         days_of_previous_month = 30  # April, June, September, November have 30 days
#     elif month == 2: #February has either 28 or 29 days
#         if year % 4 == 0:
#             if year % 100 == 0:
#                 if year % 400 == 0:
#                     days_of_previous_month = 29
#                 else:
#                     days_of_previous_month = 28
#             else:
#                 days_of_previous_month = 29
#         else:
#             days_of_previous_month = 28
#
#     day = days_of_previous_month + day - 5

# print(f"Five days ago it was: {dt.datetime(year=year, month=month, day=day).strftime('%d/%m/%Y')}")

date = dt.datetime.now()
date -= dt.timedelta(days=5)

print(f"Five days ago was {date.strftime('%d/%m/%Y')}")
