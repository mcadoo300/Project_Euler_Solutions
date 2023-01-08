import math

import prime_time


# returns if number = 2 * some square number
def is_halfsqr(number):
    half = number / 2
    sqroot = math.sqrt(half)
    if sqroot.is_integer():
        return True
    return False


def odd_property(number):
    primes_list = prime_time.list_primes_under(number)
    for prime1 in primes_list:
        difference = number - prime1
        if is_halfsqr(difference):
            return True
    return False


i = 1
flag = True
while flag:
    odd_num = 2*i + 1
    if not prime_time.is_prime(odd_num):
        flag = odd_property(odd_num)
    else:
        pass
    i += 1


print(odd_num)
