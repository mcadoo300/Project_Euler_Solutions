import prime_time

global digits
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# checks a number for a digit
def check_for_digit(dig, num):
    str_val = str(num)
    for x in str_val:
        if dig == int(x):
            return True
    return False


def get_digits_from(x):
    str_val3 = str(x)
    dig_list = []
    for x in str_val3:
        dig_list.append(int(x))
    return dig_list


def is_pan(str_val2):
    str_val2 = str_val2.replace(".", "")
    str_val2 = str_val2.replace("0", "")
    for dig in digits:
        if str_val2.count(str(dig)) != 1:
            return False
    if len(str_val2) == len(digits):
        return True
    return False


def check_pan_prod(x):
    divisors = prime_time.get_divisors(x)
    digits_in_number = get_digits_from(x)
    digits_in_number.append(0)
    for y in digits_in_number:
        for divisor in divisors:
            if check_for_digit(y, divisor):
                divisors.remove(divisor)
    if len(divisors) == 0:
        return False
    for n in divisors:
        check1 = x / n
        if divisors.count(check1) == 1:
            string_val1 = str(n) + str(check1) + str(x)
            if is_pan(string_val1):
                return True
    return False


def run_solution():
    total_sum = 0
    for i in range(1000, 9000):
        if check_for_digit(0, i):
            pass
        else:
            str_val = str(i)
            flag = True
            for d in digits:
                if str_val.count(str(d)) > 1:
                    flag = False
                    break
            if flag:
                if check_pan_prod(i):
                    total_sum += i
                    print(i)

    print(total_sum)

# run_solution()
