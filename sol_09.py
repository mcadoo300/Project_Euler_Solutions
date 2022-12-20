import math
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 1
c = 1
flag = 0
while a < 998 and flag == 0:
    for b in range(2,(998-a)):
        c = a**2 + b**2
        if math.sqrt(c)+a+b == 1000:
            flag = math.sqrt(c) * a * b
    a += 1

print(flag)
