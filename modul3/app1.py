def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def primes(limit):
    result = []
    for i in range(1, limit + 1):
        if is_prime(i):
            result.append(i)
    return result


if __name__ == '__main__':
    print(primes(17))
