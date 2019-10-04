

# counting from 1 to 20 inclusive in fizzbuzz fashion
# if the # is divisible by 3 say fizz
# if its divisible by 5 say buzz
# if its divisible by 3 and 5 say fizzbuzz
# otherwise repeat the number

def say_fizzbuzz():
    """Return fizz, buzz, fizzbuzz or just the numbers"""

    for num in range(1, 21):
        if (num % 3 == 0) and (num % 5 == 0):
            print ("fizzbuzz")
        elif num % 3 == 0:
            print ("fizz")
        elif num % 5 == 0:
            print ("buzz")
        else:
            print (num)

say_fizzbuzz()

# Runtime: O(n)
# Space complexity: O(1)
# Note: the second number in range is exclusive
