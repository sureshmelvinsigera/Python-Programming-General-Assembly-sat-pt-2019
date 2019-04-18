import datetime

today = datetime.date.today()
print(today)
print(today.month)
print(today.year)

print('==================')
now = datetime.datetime.now()
print(now)

# The strftime() Method

time = datetime.datetime.now()

print('Weekday, short version', time.strftime("%a"))
print('Weekday, full version', time.strftime("%A"))
print('Weekday as a number 0-6, 0 is Sunday', time.strftime("%w"))
print('Month name, short version', time.strftime("%b"))
print('Month name, full version', time.strftime("%B"))
print('Month as a number 01-12', time.strftime("%m"))
print('AM/PM', time.strftime("%p"))
print('Year, short version, without century', time.strftime("%Y"))
print('Year, full version', time.strftime("%y"))
print('Year, full version', time.strftime("%y"))
