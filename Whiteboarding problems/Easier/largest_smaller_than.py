
# given an ordered list of number and a number. Return the index of the largest number in the list that is smaller than the given number

# Q: What if there is no number smaller than the given number? Return None

# def largest_smaller_than(ordered_list, given_num):
#     """Return the index of the largest number in the list that is smaller than given number"""


#     # since our list is sorted, if the first number
#     # is bigger, a smaller number isn't in our list
#     # Else, loop through and return the index right before the first number
#     # that is too big
#     for i, num in enumerate(ordered_list):
#         if num > given_num:
#             if i != 0:
#                 return (i-1)
#             else: 
#                 return None
#         # if the last number isn't too big, it's the answer
#         else:
#             return -1

#     return None

# Runtime: O(n)
# Space: O(1)


# Can you find a better runtime for this? There is an O(log n) solution.

# Given that our list is sorted, we can search it more quickly than having to scan each item. Instead, we can use the principle of binary search to search it.
# We could write the binary search code ourself, but Python has a built-in library, bisect, that does this for us

def largest_smaller_than(nums, xnumber):

    from bisect import bisect_left

    # Fail-fast optimization: since our list is sorted, if the first number
    # is bigger, a smaller number isn't in our list

    if nums[0] > xnumber:
        return None

    # Locate the insertion point for xnumber in nums to maintain sorted order
    # If xnumber is already present in nums, the insertion point of bisect left will be before (to the left of) any existing entries 
    # whereas bisect right will return the insertion point which is to the right of any existing entries
    insertion_point = bisect_left(nums, xnumber)
    # print(insertion_point)

    return insertion_point 


print(largest_smaller_than([-1, 2, 3, 7, 8], 9))
print(largest_smaller_than([-2, 3, 4, 5], -4))




