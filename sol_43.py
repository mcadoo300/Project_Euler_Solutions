# for is_pan
# augment digits to 0-9
import math

import sol_32

global divisors
divisors = [1, 3, 5, 7, 11, 13, 17]


def get_nth_digit(num, n):
    str_val = str(num)
    return int(str_val[n - 1])


def check_property(num):
    # filler 0s
    digits = []
    for i in range(0, 10):
        digits.append(num[i])
    k = 0
    prod = ""
    for i in range(1, 8):
        prod += str(digits[i])
        prod += str(digits[i + 1])
        prod += str(digits[i + 2])
        if int(prod) % divisors[k] != 0:
            return k
        k += 1
        prod = ""
    return -1


def get_number(list_num):
    str_list = ""
    for x in list_num:
        str_list += str(x)
    return int(str_list)


