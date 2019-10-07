# return True if a number is a prime

# only number that is greater than 1 can be prime

# prime numbers will have no divisors other than itself and 1


def is_prime(num):
    """Return True if a number is prime"""

    num = int(num)

    if num < 2:
        return False

    # This is a very naive check -- firstly, we could check once
    # for even numbers and then count up by twos. Secondly, we
    # only have to check up to sqrt(num) -- since if a number is
    # divisible by a number > its square root, the other divisor
    # would be definition be less than its square root.

    else:
        for divisor in range(2, num):
            if (num % divisor == 0):
                return False
        return True

print(is_prime(99))

Runtime: O(n)
Space: O(1)