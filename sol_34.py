import math

fact = 1
for i in range(1, 10):
    fact *= i

upper_limit = fact * 7


def sum_factorial(x):
    string_val = str(x)
    fact_sum = 0
    for digit in string_val:
        fact_sum += math.factorial(int(digit))
    return fact_sum


total_sum = 0
for num in range(3, upper_limit + 1):
    if num == sum_factorial(num):
        total_sum += num

print(total_sum)

