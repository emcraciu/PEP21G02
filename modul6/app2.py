# Create a class for an object that inherits all the attributes of a number but can also be iterated
# example: number 3 should be iterated as 1,2,3

class MyNumber(int):
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return MyNumberIter(self.number)

    # when adding numbers we make sure we get back an iterable number object
    def __add__(self, x):
        # super allows us to use __add__ method from inherited int class
        result = super().__add__(x)
        return MyNumber(result)


class MyNumberIter:
    def __init__(self, number1):
        self.number_list = [i for i in range(1, number1 + 1)]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.number_list:
            raise StopIteration
        return self.number_list.pop(0)


if __name__ == '__main__':
    seven = MyNumber(7)
    five = MyNumber(5)

    for value in five:
        print('Iterating number 5:', value)

    print(80 * '#')
    # adding objects created with our class
    add_result = seven + five

    for value in add_result:
        print('Iterating number 5+7:', value)
