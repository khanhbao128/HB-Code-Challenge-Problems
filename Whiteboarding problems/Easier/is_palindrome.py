
# return True if a word is a palindrome? A palindrome is a word that is spelled the same forwards and backwards

# Should we treat spaces, upper and lower cases normally? Yes

# def is_palindrome(word):
#     """Return True if a word is a palindrome"""

#     backwards = word[::-1]
#     if word == backwards:
#         return True
#     return False

# Runtime: O(1)
# Space: O(n)


# other solution
def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False

    return True

# Runtime: O(n)
# Space : O(1)

print(is_palindrome('Racecar'))
print(is_palindrome('race car'))
print(is_palindrome('racecar'))

# double check runtime and space complexities in both cases
