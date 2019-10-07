

# Is the word an anagram of a palindrome?

# A palindrome is a word that reads the same forward and backwards (eg, “racecar”, “tacocat”). An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).

# Determine if the given word is a re-scrambling of a palindrome.

# The word will only contain lowercase letters, a-z.

# Don’t Care If It’s Real English Word

# Verify: palindrome is any word that reads the same forward and backwards
#         anagram is a rescrambling of a word
#         >>need to determine if a word is a rescrambling of a palindrome


def anagram_of_palindrome(word):
    """ return True if a word an anagram of a palindrome"""

    seen = {}
    for letter in word:
        count = seen.get(letter, 0)
        seen[letter] = count + 1

    num_oddcounts = 0
    for count in seen.values():
        if count % 2 != 0:
            num_oddcounts += 1


    # a palindrome will have a number of odd counts to be either 0 or 1
    if num_oddcounts > 1:
        return False
    return True

print(anagram_of_palindrome('booeeoboe'))

# Runtime: O(2n)
# Space O(n)

# The algorithm here is that anagrams of palindromes must have an even number of all letters but one 
# (it’s fine if one letter has an odd number of occurrences, as that could be the middle letter, 
# but if more than one letter has an odd number of occurrences, it can’t be an anagram of a palindrome).




