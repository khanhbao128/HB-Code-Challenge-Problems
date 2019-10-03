# given a list of integer. Return True if any 2 numbers sum to 0


# Q: How about a list that contains 0? >>always return True if there is a 0

def add_to_zero(given_list):
    """Return True if any 2 numbers in list sum to 0"""

    # create an empty dictionary to save all the integer that are already checked in the list
    seen = {}

    # loop through each integer in the list
    # find the number that can be added to the integer to make 0
    for num in given_list:
        if num == 0:
            return True
        opposite_num = 0 - num
        if opposite_num in seen:
            return True
        else:
            seen[num] = True
    return False

# print(add_to_zero([-2, 4, 8, 2]))
# print(add_to_zero([4, 1, 5, 3, -1, 9]))
# print(add_to_zero([-1, 3, 5, 0]))
# print(add_to_zero([1, 2, 3]))

# Better version

def add_to_zero(given_list):

    # make a copy of the given_list but turn it into a set to make searching a lot faster O(1)
    set_list = set(given_list)

    # for each num in the list find if its -n in the set (-0==0 in Python)
    for num in given_list:
        if -num in set_list:
            return True
    return False

print(add_to_zero([0, 1, 3]))
print(add_to_zero([1, 3, 5, -1]))
print(add_to_zero([1, 2, -2, 1]))


