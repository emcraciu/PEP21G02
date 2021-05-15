""" Homework 4  - needs to be presented before exam day"""


# We want to check which of the following function has the smallest minimum for x in range -10, 10 and use that function
# to calculate for x = 0
# 1x^2 -2x + 2
# 2x^2 -4x + 4
# 3x^2 -6x + 6

# 20P
# Create a function (build) that takes 3 int arguments (a, b, c) and return a function (response) that takes one int
# argument (x) and calculates ax^2+bx+c

def build(a, b, c):
    pass  # <your code here>


# 20P
# Create a list of response functions by calling build function with the arguments (1,-2,3), (2,-4,4), (3,-6,5)
list_of_functions = []
for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    pass  # <your code here>

# 20P
# Create a dictionary that contains the result functions as keys and as values the list of results from calling that
# function with x in range -10, 10 as value
dict_of_results = {}
for function in list_of_functions:
    pass  # <your code here>

# 20P
# Check dict_of_results and determine which function has the smallest value in the list of values
function_with_smallest_result = None
smallest_value = None
for function, values in dict_of_results.items():
    pass  # <your code here>

# 20P
# Call function_with_smallest_result with argument x = 0 and print the returned value (you should get 2)
pass  # <your code here>
