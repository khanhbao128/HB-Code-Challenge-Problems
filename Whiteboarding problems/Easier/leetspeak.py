
# some standard characters are replaced by numeral or special characters

def translate_leet(phrase):
    """Replace some standard characters with numerical or special characters"""

    leet_speak = {
            'a': '@',
            'o': '0',
            'e': '3',
            'l': '1',
            's': '5',
            't': '7',
        }

    leet_phrase = ''

    for char in phrase:
        leet_phrase += leet_speak.get(char.lower(), char)

    return leet_phrase

# Runtime: O(n*2)
# loopthrough each char in phrase takes O(n) time 
# Also adding each char to a string takes O(n) time as well since string is immutable. We r not adding to the end of the string but building up the new string each time

print(translate_leet("Hi Balloonicorn"))





