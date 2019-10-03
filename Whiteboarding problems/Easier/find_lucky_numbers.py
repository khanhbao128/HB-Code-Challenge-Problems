
# given an integer n. Return a list of n unique numbers from 1 to 10 inclusive
# n will never be smaller than 0 or bigger than 10

# Q: Can n be 0? yes return []

import random

# def find_n_numbers(n):
#     """Return a list of n unique numbers"""

#     # create a counter i which goes from 0 to n - 1. 
#     # Once n reaches n - 1 stop generating any more numbers
#     desire_list = []

#     if n == 0:
#         return desire_list

#     else:
#         i = 1
#         while i <= n:
#             num = random.randint(1, 10)
#             if num in desire_list:
#                 i = i 
#             else: 
#                 desire_list.append(num)
#                 i = i + 1
                
#         return sorted(desire_list)


# print(find_n_numbers(3))
# print(find_n_numbers(0))

# Runtime: O(n^2)

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    # use list to turn range(1,11) into a list of numbers from 1 to 10
    nums = list(range(1, 11))
    lucky_nums = []

    for i in range(n):
        num = random.choice(nums)
        nums.remove(num)
        lucky_nums.append(num)

    return lucky_nums

print(lucky_numbers(3))
print(lucky_numbers(0))

# This solution's runtime is O(n) which is a lot faster than the above solution
# The great thing about the below solution is that it creates another list of all nums from 1 to 10
# Each time a number is generated from this list, it will then be removed from the list so python will not generate a duplicate number
# random.randint(1,10)
# random.choice(list)
