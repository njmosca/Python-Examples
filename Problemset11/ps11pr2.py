#
# ps11pr2.py (Problem Set 11, Problem 2)
#
# A class to represent calendar dates
#Author: Nicholas Mosca










class Date:
    """ A class that stores and manipulates dates,
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    def advance_one(self):
        ''' advances the date called by one day'''
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # if the day is equal to one of the max days for that month
        self.day += 1
        if self.is_leap_year():
            days_in_month[2] = 29
        # is this day valid
        if self.day > days_in_month[self.month]:
            self.month += 1
            self.day = 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        




    def advance_n(self,n):
        ''' advacnes day by n days'''
        if n == 0:
            print(self)
        else:
            print(self)
            for day in range(n):
             self.advance_one()
             print(self)
    

    def __eq__(self,other):
        ''' compares self(date with other date) deep check not just comparing memory location'''
        return(self.day == other.day and self.month == other.month and self.year == other.year)

    def is_before(self,other):
        ''' compares two dates and returns true if other is before self'''
        if self == other:
            return False
        elif self.year < other.year:
            return True
        elif self.year <= other.year and self.month < other.month:
            return True
        elif self.year <= other.year and self.month <= other.month and self.day < other.day:
            return True
        else:
            return False
                
    def is_after(self,other):
        ''' returns true is self comes after other'''
        if self == other:
            return False
        elif self.is_before(other) == False:
            return True
        else:
            return False 
           
    
    def days_between(self,other):
        ''' returns the integer representing the amount of days between self and other'''
        new_self = self.copy()
        new_other = other.copy()
        count = 0

        if new_self == new_other:
            return 0

        elif new_self.is_before(new_other):
            
            while new_self != new_other:
                #print('new_self is',new_self,'new_other is',new_other)
                new_self.advance_one()
                count -= 1    
        else: 
            while new_other != new_self:
                new_other.advance_one()
                #print('new_self is',new_self,'new_other is',new_other)   
                count += 1      
        return count
        
    def day_name(self):
        ''' returns the day of the week of a date'''
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_date = Date(4,8,2019) #monday
        days_between = self.days_between(start_date)
        weekday = day_names[(days_between % 7)]

        #print('days_between is',days_between)
        
        return weekday
        
        






