import math
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(x):
    if x % 2 == 0:
        x /= 2
        prev_factor = 2
        while x % 2 == 0:
            x /= 2
    else:
        prev_factor = 1

    factor = 3
    max_factor = math.sqrt(x)
    while x > 1 and factor <= max_factor:
        if x % factor == 0:
            x /= factor
            prev_factor = factor
            while x % factor == 0:
                x /= factor
            max_factor = math.sqrt(x)
        factor += 2
    if x == 1:
        return prev_factor
    else:
        return x

print(largest_prime_factor(600851475143))