
# check if a sentence is a pangram. 
# A pangram is a sentence that contains all the letters of the English alphabet at least once

def is_pangram(sentence):
    """Return True if a sentence is a pangram"""

    sentence = sentence.rstrip()
    words = sentence.split()
    letters = "".join(words)
    # turn the string into all lower cases and also a set bc set doesn't contain duplicates
    letters = letters.lower()
    letters = set(letters)

    if len(letters) == 26:
        return True

    else:
        return False


print(is_pangram('The quick brown fox jumps over the lazy dog'))