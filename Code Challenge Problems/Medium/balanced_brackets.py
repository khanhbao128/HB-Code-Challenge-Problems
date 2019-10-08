
# return True if a phrase's opening and closing brackets are balanced
# there are 4 types of opening and closing brackets: <>, (), {}, []
# if a phrase has non opening or closing bracketss, return True
# the order of opening and closing brackets matter

def balanced_brackets(phrase):
    """Return True if a phrase has balanced brackets"""

    # since 1 type of closers will match only 1 type of openers, set up a dictionary to form the relationships between different types of closers and openers
    # Notice that the closers_to_openers dictionary uses the closing brackets as keys, rather than the opening brackets. 
    # This lets us more easily compare the opening bracket on the top of the stack to any arbitrary closing bracket’s matching opener.
    closers_to_openers = {'>':'<', ')':'(', '}':'{', ']':'['}

    # set of all openers to match openers quickly
    openers = set(closers_to_openers.values())
    # create an empty list and use it as a stack
    openers_seen = []

    for char in phrase:
    # loop through char, push any openers found onto the openers_seen stack
        if char in openers:
            openers_seen.append(char)
    # once find a closer, check the openers_seen stack, if its empty, it fails fast
        elif char in closers_to_openers:
            if openers_seen == []:
                return False
            # if the stack is not empty, then check if the opener of the closer just found matches the last opener in the seen stack
            elif openers_seen[-1] == closers_to_openers.get(char):
                openers_seen.pop()
            # if closer found does not match the last and the stack is not empty either
            else:
                return False
    # at the end if the openers_seen is empty return True
    return openers_seen == []


print(balanced_brackets('hello({[<world)'))
print(balanced_brackets('hello'))
print(balanced_brackets('hello([world])'))
