# for is_pan
import sol_32


def form_concat_prod(number, n):
    string_rtrn = ""
    for i in range(1, n + 1):
        string_rtrn += str(number * i)
    return string_rtrn


def get_upper_n(number):
    num_digits = 9
    k = 1
    while num_digits > 0:
        new_num = str(number * k)
        num_digits -= len(new_num)
        k += 1
    k -= 1
    if num_digits <= -1:
        return -1
    else:
        return k


largest_pan_dig = 0

for i in range(1, 10000):
    m = get_upper_n(i)
    test5 = form_concat_prod(i, m)
    if sol_32.is_pan(test5):
        if largest_pan_dig < int(test5):
            largest_pan_dig = int(test5)

print(largest_pan_dig)
