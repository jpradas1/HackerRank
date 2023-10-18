'''
Calendar Module
The calendar module allows you to output calendars and provides additional 
useful functions for them.

    class calendar.TextCalendar([firstweekday])

This class can be used to generate plain text calendars.

TASK
You are given a date. Your task is to find what the day is on that date.
'''

from calendar import weekday, weekheader

if __name__=='__main__':
    month, day, year = list(map(int, input().split()))
    days = [x.strip().upper() for x in weekheader(10).split(' ') if x]
    print(days[weekday(year=year, month=month, day=day)])