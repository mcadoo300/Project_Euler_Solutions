import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number = []
count = 1000000
digit_num = 9
while digit_num > -1:
    i = 1
    while i * math.factorial(digit_num) < count:
        i += 1
    i -= 1
    count -= i * math.factorial(digit_num)
    number.append(digits[i])
    digits.remove(digits[i])
    digit_num -= 1
print(number)

