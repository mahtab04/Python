import datetime
currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)
print(currentDate.strftime('%d %b, %y'))
currentDate = datetime.datetime.now()
print(currentDate.minute)
print(currentDate.hour)
print(currentDate.second)
