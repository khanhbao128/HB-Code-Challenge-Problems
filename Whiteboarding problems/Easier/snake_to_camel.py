
# given a variable name written in snake_case
# Return the new string with that name written in camelCase

def snake_to_camel(name):
    """Turn a snake cased name to a camel cased name"""

    words = name.split('_')
    
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()
    return ''.join(words)

print(snake_to_camel('snake_to_camel'))