
# define a function that takes in 3 numbers and return the largest 

def max_of_three(num1, num2, num3):
    """Return the largest number in three numbers given"""

    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    elif num3 >= num1 and num3 >= num2:
        return num3

    else: 
        return "Something went wrong"

print(max_of_three(10, 1, 11))

