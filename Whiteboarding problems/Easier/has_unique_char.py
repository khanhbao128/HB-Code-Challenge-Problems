

# given a word. Return True if word contains only unique characters

# Q: do we need to consider lower cases and upper cases separately? Yes

# def has_unique_char(word):
#     """Return True if a word contains unique characters"""

#     seen = {}

#     for char in word:
#         if char not in seen:
#             seen[char] = True
#         else:
#             return False
#     return True


# Runtime: O(n)
# Space Complexity: O(n)

# Another great solution:

def has_unique_char(word):

    unique_word = set(word)

    return len(word) == len(unique_word)

print(has_unique_char('LOop'))
print(has_unique_char('unique'))

Runtime: O(1)
Space O(1)
