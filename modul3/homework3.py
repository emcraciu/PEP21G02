""" Homework 3 - needs to be presented before exam day"""


# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have their length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

def ordered_ints(list_of_objects: list):
    pass
    # <your code here>


print(ordered_ints([1, True, '123', False, 6, ()]))


# 25P - (use recursion)
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2

def sum_of_square(n: int):
    pass
    # <your code here>


print(sum_of_square(10))


# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)*(2^2)*(3^2)

def factorial_of_squares(n: int):
    pass
    # <your code here>


print(factorial_of_squares(5))


# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower-case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become ("1234567A", "_ext_to_te_t")

def process_text(text: str):
    pass
    # <your code here>


print(process_text('1234567a Text to te5t'))
