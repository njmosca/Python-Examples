#
# ps12pr1.py (Problem Set 12, Problem 1)
#
# More Date clients programs
#

# this import statement will allow your to use the Date class from ps11pr2.py
from ps11pr2 import Date

def nye_counts(start, end):
    ''' determines which day nye falls on from range of dates'''

    d = {'Saturday':0 , 'Thursday': 0, 'Monday': 0, 'Sunday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Friday': 0} # create an empty dictionary

    # add your code here
    for year in range(start,end +1):
        nye = Date(12,31,year)
        nye_day = nye.day_name()
        if nye_day not in d:

            d[nye_day] = 1
        else:
            d[nye_day] += 1
    return d
    
