import prime_time
import math

list_primes = prime_time.list_primes_under(100000)


def quad_formula(n, x, y):
    rtrn_val = n ** 2 + x * n + y
    return rtrn_val


i = 0
consecutive_prime = 0
prod_list = [0,0]
longest_list = 0
a = -999
b = -1000

while a < 1000:
    while b < 1001:
        z = quad_formula(i, a, b)
        while prime_time.is_prime(z):
            consecutive_prime += 1
            i += 1
            z = quad_formula(i, a, b)
        if consecutive_prime > longest_list:
            longest_list = consecutive_prime
            prod_list[0] = a
            prod_list[1] = b

        consecutive_prime = 0
        i = 0
        b += 1
    b = -1000
    a += 1

print(prod_list[0] * prod_list[1])
