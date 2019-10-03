
# given 2 list. Concatenate them

# Q: If one list is empty>>> return the other list that is not empty 
# Q: if both lists are empty>>> return an empty list

def concatenate_lists(list_1, list_2):
    """Return the concatenation of 2 lists"""

    # check if both lists are empty
    if not list_1 and not list_2:
        return []
    # check if first list is empty
    elif not list_1:
        return list_2
    # check if second list is empty
    elif not list_2:
        return list_1

    # if either list is empty
    else:
        for num in list_2:
            list_1.append(num)

    return list_1

print(concatenate_lists([0, 2, 4, 5], [6, 7, 8]))
print(concatenate_lists([], [9, 4, 5]))
print(concatenate_lists([3, 4], []))
print(concatenate_lists([], []))

# SOLUTION
# def concat_lists(list1, list2):
#     """Combine lists."""

#     # START SOLUTION

#     for item in list2:
#         list1.append(item)

#     return list1