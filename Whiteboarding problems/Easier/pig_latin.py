
# turn a phrase into pig latin (there are spaces separate the words). There is no punctuations in phrase
# rule: if word begins with consonants, move first letter to the end and add yay
        # if word begins with vowels, add yay to the end

def pigLatin_word(word):
    """Turn a word into a pig latin word"""

    if word[0] in 'aeoiu':
        return word + 'yay'
    else:
        return word[1:] + word[0] + 'yay'
  

def translate_to_pigLatin(phrase):
    """Translate a phrase into pig Latin"""

    # split() method removes all the spaces and turn a phrase into a list of words
    # by default split() remove spaces, don't need to include " " in ()
    words = phrase.split()
    new_phrase = []
    for word in words:
        new_phrase.append(pigLatin_word(word))
        
    return ' '.join(new_phrase)

print(translate_to_pigLatin('porcupines are cute'))

# Runtime: O(n)
# Space: O(n)

# Runtime: O(n*2)
# Space: O(n)