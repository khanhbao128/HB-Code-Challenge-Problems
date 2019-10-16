
# given a list of items, return the new list of items in the same order but with all duplicates removed
# Q: what does an empty list return? empty list

def deduped(items):
    """Remove all duplicates in a list and return the new list of items in the same order"""

    # new_list = []
    # for item in items:
    #     if item not in new_list:
    #         new_list.append(item)
    # return new_list

    # Runtime: O(n*2) >> bc have to look at each item in new_list to make sure item not in new_list
    # >> to improve runtime, create a set called seen and check item against the set
    # better solution
    seen = set()
    new_list = []
    for item in items:
        if item not in seen:
            new_list.append(item)
            seen.add(item)
    return new_list

print(deduped([1, 2, 1, 1, 3]))



