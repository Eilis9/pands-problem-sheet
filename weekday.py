"""
Week 5 assignment
Program which prints if the current day is a weekday or weekend
Author: Eilis Donohue
Ref: PYnative.com/python-get-the-day-of=week
"""

# import the datetime class from the datetime module
from datetime import datetime
# assign the current date and time to dt
dt = datetime.now()

# weekday method to find day of week - returns integer
x = dt.weekday()

# checks value of x - prints accordingly
if x == 6 or x == 7:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")