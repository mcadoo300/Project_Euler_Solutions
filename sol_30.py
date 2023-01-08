power_sum = 9 ** 5
num_digit = 1
while 10 ** num_digit < power_sum * num_digit:
    num_digit += 1

upper_bound = power_sum * (num_digit - 1)


def fact_sum(number):
    factor_sum = 0
    str_val = str(number)
    for x in str_val:
        factor_sum += int(x) ** 5
    return factor_sum


solution_sum = 0
for n in range(10,upper_bound + 1):
    if n == fact_sum(n):
        solution_sum += n
print(solution_sum)
