

# Given a word (no spaces no punctuations) in English, return True if that word contains more vowels than non-vowels; otherwise, return False. The word will always be a single word, without any punctuation or spaces. It will contain only uppercase and lowercase letters.

# If the phrase is over half vowels, it should return True
# y is not a vowel

# Q: What if the numbers of vowels and non-vowels are equal? >> return False

def has_more_vowel(word):
    """Return True if a word is overly half vowels"""

    num_vow = 0 

    for letter in word:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            num_vow += 1
        else:
            num_not_vow += 1
    return num_vow > len(word)/2


print(has_more_vowel('chimney'))
print(has_more_vowel('room'))
print(has_more_vowel('boo'))


# Runtime: O(n)
# Space complexity: O(1)
# NOTE: when a problem wants to return either True or False: can include the statement that needs to be proved in the return statement instead of writing another line of if statement


