# common functions dealing with primes
import math


# get prime factorization as a 2-d array
# that is : x = p**a * q**b *...* r**n (where p,q,r... are prime and a,b,n,... are exponents
def prime_factorization(x):
    if x % 2 == 0:
        x /= 2
        a = 1
        while x % 2 == 0:
            a += 1
            x /= 2
        prime_list = [[2], [a]]
        # prime factor = prime_list[0][i]**prime_list[1][i]

    else:
        prime_list = [[], []]

    factor = 3
    max_factor = math.sqrt(x)
    while x > 1 and factor <= max_factor:
        if x % factor == 0:
            x /= factor
            a = 1
            while x % factor == 0:
                x /= factor
                a += 1
            prime_list[0].append(factor)
            prime_list[1].append(a)
            max_factor = math.sqrt(x)
        factor += 2
    if x == 1:
        return prime_list
    else:
        prime_list[0].append(x)
        prime_list[1].append(1)
        return prime_list


def list_prime_factors(x):
    list1 = prime_factorization(x)
    return list1[0]


# get largest prime factor
# calls get_primes then returns most recently added item(largest prime)
def largest_prime_factor(x):
    var = list_prime_factors(x)
    return var.pop(len(var) - 1)


# return number of divisors of some number x
def get_num_divisors(x):
    factors = prime_factorization(x)
    num_divisors = 1
    for a in factors[1]:
        num_divisors *= (a + 1)
    return num_divisors


# list primes under x
def list_primes_under(x):
    prime_list = [True] * x
    prime_list[0] = False
    if x != 1:
        prime_list[1] = False

    for i in range(2, int(math.sqrt(x) + 1)):
        if prime_list[i]:
            index = i * 2
            while index < x:
                prime_list[index] = False
                index += i

    prime = []

    for i in range(x):
        if prime_list[i]:
            prime.append(i)
    return prime


# works for n <= 100000+-
def list_first_n_primes(n):
    var = list_primes_under(2000000)
    primes = []
    for i in range(n):
        primes.append(var[i])
    return primes


# is x prime
def is_prime(x):
    x = abs(x)
    if x == 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True
    upper_bound = math.floor(math.sqrt(x)) + 1
    sieve = list_primes_under(upper_bound)
    for y in sieve:
        if x % y == 0:
            return False
    return True


def get_divisors(x):
    divisors = []
    for n in range(1,math.ceil(x/2)):
        if x % n == 0:
            if divisors.count(n) == 0:
                divisors.append(n)
    return divisors
