
# find the longest words in a list and return its length

def find_longest(word_list):
    """Find and return the longest words in the list"""

    # Solution 1
    # return max([len(word) for word in word_list])

    # Solution 2
    # Python’s max function finds the biggest thing in a list (or set or tuple) — but it also take a second argument, a “key” function which it can use to determine how to judge which is the biggest
    # return the len of the word in the list that has the max length
    return len(max(word_list, key=len))

    
print(find_longest(["Balloonicorn", "Hackbright"]))


