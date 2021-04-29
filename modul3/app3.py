def add_numbers():
    result = 0
    numbers = []
    while result <= 100:
        if result == 100:
            break
        number = int(input("Enter numbers: "))
        if number >= 0:
            result += number
            numbers.append(number)
    else:
        return result
    return numbers


if __name__ == '__main__':
    print(add_numbers())
