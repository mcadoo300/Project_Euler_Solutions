import math


def get_digit(n):
    i = 0
    digits_passed = 0
    # number of digits in "sector"
    while n > digits_passed:
        digits_passed += 9 * (10 ** i) * (i + 1)
        i += 1
    digits_passed -= 9 * (10 ** (i-1)) * i
    possible_digits = []
    num_digits = i
    while i > 1:
        k = 1
        while n > digits_passed:
            digits_passed += 10**(i-1) * 2
            k += 1
        k -= 1
        possible_digits.append(k)
        digits_passed -= 10**(i-1) * 2
        i -= 1


print(get_digit(17))
