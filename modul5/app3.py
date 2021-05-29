# take two values from input and divide them:


def divide_values():
    try:
        x1 = int(input("Enter first number:"))
        x2 = int(input("Enter second number:"))
    except ValueError:
        print("You should enter a number 1-9")
        return None
    try:
        my_divide = x1 / x2
    except ZeroDivisionError:
        print('You should not divide by zero')
    else:
        return my_divide


if __name__ == '__main__':
    print('Result is:', divide_values())
