#!/usr/bin/env python3

import datetime
from dateutil.rrule import rrule, YEARLY, MONTHLY, WEEKLY

startday = datetime.date(1985, 12, 11)
today = datetime.date.today()
#today = datetime.date(2022,12,11)

diff = today - startday
days = diff.days
print('Hours: ', days*24)
print('Days: ', days)
print('Weeks: ', days//7)
months = [dt for dt in rrule(MONTHLY, dtstart=startday, until=today)]
print('Months: ', len(months)-1)
#weeks = [dt for dt in rrule(WEEKLY, dtstart=startday, until=today)]
#print(len(weeks)-1)
years = [dt for dt in rrule(YEARLY, dtstart=startday, until=today)]
print('Years: ', len(years)-1)
