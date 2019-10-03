
# given a month and a year separated by a space. Return the num of days in that month

# Q: how about leap years? Are there any ways that a leap year can be determined?
# leap year is divisible by 4 or 400. If a year is divisible by 100, it is not a leap yr

def days_in_month(given_str):
    """Return number of days in a month"""

    month, year = given_str.split()
    month = int(month)
    year = int(year)

    print("month", month, "year", year)

    if month == 2:
        print('month2', month)
        if (year % 4 == 0) or (year % 400 == 0):
            print('year4+400', year)
            return 29
        elif (year % 100 == 0):
            print('year100', year)
            return 28 

        else: 
            return 28

    elif month in [1, 3, 5, 7, 8, 10, 12]:
        print('last',month)
        return 31
        
    elif month in [4, 6, 9, 11]:
        print('last last', month)
        return 30

print(days_in_month('02 2019'))

# SOLUTION
# def is_leap_year(year):

#     if year % 400 == 0:
#         return True

#     if year % 100 == 0:
#         return False

#     if year % 4 == 0:
#         return True

# def days_in_month(date):
#     """How many days are there in a month?"""

#     # START SOLUTION

#     month, year = date.split()
#     month = int(month)
#     year = int(year)

#     # Account for February

#     if month == 2:
#         if is_leap_year(year):
#             return 29
#         else:
#             return 28

#     if month in {1, 3, 5, 7, 8, 10, 12}:
#         return 31

#     if month in {4, 6, 9, 11}:
#         return 30
# print(days_in_month('02 2019

# NOTE: if we use multiple ifs to check if a year is a leap year, need to include the cases in which the year is not divisible by either 4, 400, 100
        # however, if we use one function to check leap year, only need to check if this function return True or else: this else means both False or None (none= not divisible by either 4, 400, 100)
