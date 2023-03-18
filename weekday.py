"""
Week 5 PANDS assignment
Author: Eilis Donohue
Description: Program which prints if the current day is a weekday or weekend
***The program is fully commented and reproduced in  README.ipynb***
"""

# import the datetime class from the datetime module
from datetime import datetime
# assign the current date and time to dt
dt = datetime.now()

# Weekday method to find day of week - returns integer
x = dt.weekday()

# checks value of x - prints accordingly
if x == 5 or x == 6:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")