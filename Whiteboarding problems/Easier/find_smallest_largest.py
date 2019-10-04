
# given a list of numbers, return the biggest and smallest numbers

# Q: what if list contains 1 number >> that number is the smallest and the largest number
# Q: what if list is empty >> return None

find_range(num_list):
    """Return the smallest and largest numbers in a list of integers"""

    if len(num_list) == 0:
        return None

    elif len(num_list) == 1:
        for num in num_list:
            return (num, num)

    else:
        for num in num_list: 
             