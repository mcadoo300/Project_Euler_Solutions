import math
import itertools

import prime_time

# generate list of 4 digit primes
primes_list = prime_time.list_primes_under(10000)
four_dig_primes = []
for prime1 in primes_list:
    if len(str(prime1)) == 4:
        four_dig_primes.append(prime1)


def is_prime_seq(number, x):
    for i in range(1, 3):
        if four_dig_primes.count(number + i * x) != 1:
            return False
    return True


def get_string_seq(number, x):
    string_rtrn = ""
    for i in range(3):
        string_rtrn += str(number + (i * x))
    return string_rtrn


def get_number(d):
    string_val = ""
    for n in d:
        if str(n).isdigit():
            string_val += str(n)
    string_val = string_val.replace("'", "")
    return int(string_val)


def get_prime_permutations(num):
    string_val = str(num)
    digits = []
    for x in string_val:
        digits.append(int(x))
    permutations1 = list(itertools.permutations(digits))
    permutations2 = []
    for x in permutations1:
        if four_dig_primes.count(get_number(x)) == 1:
            permutations2.append(get_number(x))
    while permutations2.count(num) > 0:
        permutations2.remove(num)
    permutations2.sort()
    return permutations2


string_concat = []

"""for num1 in four_dig_primes:
    prime_perm = get_prime_permutations(num1)
    if len(prime_perm) < 2:
        pass
    else:
        k = 0
        while k < len(prime_perm) - 1:
            difference = num1 - prime_perm[k]
            if is_prime_seq(num1, difference):
                string_concat.append(get_string_seq(num1,difference))
                break
            elif (num1 + (2*difference)) > prime_perm[len(prime_perm)-1]:
                break
    if len(string_concat) == 2:
        break
"""

print(string_concat)
