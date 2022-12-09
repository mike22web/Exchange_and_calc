# 2 algorithms for checking whether a number is prime are shown.
# The "while" loop shows how much time each of them takes to work.

import timeit


def is_prime(number):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def is_prime_2(num):
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                return False
                break
        else:
            return True
    if num == 2:
        return True
    else:
        return False


while True:
    n = int(input())
    if n == 0:
        break
    else:
        time_start = timeit.default_timer()
        print(is_prime_2(n))
        time_2 = timeit.default_timer() - time_start
        print(f'time_2 - {time_2}')
        time_start_2 = timeit.default_timer()
        print(is_prime(n))
        time_1 = timeit.default_timer() - time_start_2
        print(f'time_1 - {time_1}')
        res = time_1 / time_2
        print(f'the "is_prime_2" algorithm is {round(res, 1)} times faster than "is_prime"')

num = int(input())


def count_prime(num):
    counter = 0
    for i in range(2, num):
        if is_prime_2(i):
            counter += 1
    return counter


print(count_prime(num))
