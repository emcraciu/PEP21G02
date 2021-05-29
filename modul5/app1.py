from modul3.app1 import primes
import random


def random_prime_numbers(num, limit):
    fin_list = []
    my_list = primes(limit)
    y = len(my_list)
    for _ in range(num):
        x = random.randint(0, y - 1)
        fin_list.append(my_list.pop(x))
        y -= 1
    print(fin_list)


random_prime_numbers(5, 100)
