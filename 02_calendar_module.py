import calendar

print(calendar.weekheader(3)) # giving the header of the week length of 3.

print(calendar.firstweekday())
print(calendar.month(2049, 8)) # August of 2049 calendar.

print(calendar.monthcalendar(2049, 8)) # 2D array matrix of the days in August.

print(calendar.calendar(2049)) # the entire year calendar.

day_of_the_week = calendar.weekday(2049, 8, 22) # the index of this specific date.
print(day_of_the_week)

is_leap = calendar.isleap(2049)
print(is_leap)

days_in_leap_year = calendar.leapdays(2020, 2049)
print(days_in_leap_year)
