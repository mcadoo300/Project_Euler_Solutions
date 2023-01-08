import prime_time
import time

st = time.time()

global primes_list
primes_list = prime_time.list_primes_under(1000000)
global testing_list
testing_list = []
for prime1 in primes_list:
    if prime1 < 121312:
        pass
    else:
        testing_list.append(prime1)


# get primes with n digits
def get_primes_with_n_digits(n):
    list1 = []
    for num in testing_list:
        if len(str(num)) == n:
            list1.append(num)
        elif len(str(num)) > n:
            break
    return list1


def get_digit_n(num, n):
    str_val = str(num)
    return str_val[n - 1]


# get list of primes with same digit num and value at pos digit1
def get_prime_with_dig(value1, digit_pos):
    key = get_digit_n(value1, digit_pos)
    list2 = get_primes_with_n_digits(len(str(value1)))
    list3 = []
    for prime in list2:
        if get_digit_n(prime, digit_pos) == key:
            list3.append(prime)
    return list3


# returns if element is in list of primes
def is_in_list(x, list1):
    for i in range(len(list1)):
        if list1[i] == x:
            return True
    return False


def remove_single_occurring_digits(list3):
    repeated_digits = [[-1] * len(list3[0]) for _ in range(len(list3[0]))]
    lower_limit = len(list3) - 2
    r_count = 0
    blank_count = 0
    for row in list3:
        for n in row:
            if n == -1:
                blank_count += 1
        if blank_count != lower_limit:
            repeated_digits[r_count] = row
            r_count += 1
        blank_count = 0
    blank_count = 0
    new_list = []
    row_c = 0
    for row in repeated_digits:
        for n in row:
            if n == -1:
                blank_count += 1
        if blank_count != len(list3[0]):
            new_list.append(row)
        row_c += 1
        blank_count = 0
    return new_list


# get digit_pos of digits which are equal
def get_same_digit_placement(num):
    str_val = str(num)
    repeated_digits = [[-1] * (len(str_val) + 1) for _ in range(len(str_val) + 1)]
    pos = 1
    count = 0
    for x in str_val:
        if not is_in_list(x, repeated_digits):
            repeated_digits[count][0] = x
            count += 1
        for i in range(count):
            if repeated_digits[i][0] == x:
                insert_val = i
                break
        repeated_digits[insert_val][pos] = pos
        pos += 1
    repeated_digits = remove_single_occurring_digits(repeated_digits)
    return repeated_digits


def get_repeated_digits_pos(prime):
    raw_dat = get_same_digit_placement(prime)
    index_list = []
    for row in raw_dat:
        i = 1
        while i < len(row):
            if row[i] != -1:
                index_list.append(row[i])
            i += 1
    return index_list


# get position of non_repeating numbers
def get_nonrep_pos(prime):
    possible_primes = get_primes_with_n_digits(len(str(prime)))
    rep_digits = get_same_digit_placement(prime)
    same_digit_pos = get_repeated_digits_pos(prime)
    same_digit = []
    for n in range(1, len(str(prime)) + 1):
        if same_digit_pos.count(n) == 0:
            same_digit.append(n)
    return same_digit


# get primes that are same digit length and share non-repeating digits
def primes_with_same_digs(prime):
    same_digit = get_nonrep_pos(prime)
    test_list = []
    for pos in same_digit:
        test_list.append(get_prime_with_dig(prime, pos))

    final_list = []
    flag = False
    if len(test_list) > 0:
        for k in test_list[0]:
            for m in range(len(test_list)):
                if m != 0:
                    for q in test_list[m]:
                        if k == q:
                            flag = True
                            break
                    if not flag:
                        break
                    elif m < len(test_list) - 1:
                        flag = False
            if flag:
                final_list.append(k)
            flag = False
    return final_list


def are_digits_equal(digit_list, prime):
    string_val = str(prime)
    key = string_val[digit_list[0] - 1]
    for n in digit_list:
        if key != string_val[n - 1]:
            return False
    return True


def get_seq_list(prime):
    list1 = primes_with_same_digs(prime)
    key_digits = get_repeated_digits_pos(prime)
    return_list = []
    if len(key_digits) > 0:
        for number in list1:
            if are_digits_equal(key_digits, number):
                return_list.append(number)
    return return_list


longest_list = []
while len(longest_list) < 8:
    prime = testing_list.pop(0)
    possible_list = get_seq_list(prime)
    if len(possible_list) > 0:
        possible_list.append(prime)
        if len(possible_list) > len(longest_list):
            longest_list = possible_list

print(longest_list)
