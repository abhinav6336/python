import datetime

#CREATING DATE
d = datetime.date(2016,7,21)
print(d)

#TODAY DATE 
td = datetime.date.today()
print(td)

#GRABBING YEAR,MONTH AND DAY
day   = td.day
month = td.month
year  = td.year

#DAY NUMBER 
print(td.weekday()) #consider monday as 0 
print(td.isoweekday()) #consider monday as 1  

#TIMEDELTA TO REPRESENT DATE IN FORM OF NUMBER OF DAYS
tdelta = datetime.timedelta(days=7)
print(td+tdelta) #date_2 = date_1 + timedelta
print(td-tdelta) #timedelta = date_1 + date_2

#NO OF DAYS BETWEEN TWO DATES 
bday = datetime.date(2026,10,4)
till_bday = bday - td
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds()) #total seconds left between dates

#GETTING THE TIME 
t = datetime.time(9,30,45,10000)
print(t)
print(t.hour)

#GETTING BOTH DATE AND TIME 
tdtt = datetime.datetime(2026,6,12,6,4,2,1000)
print(tdtt)

