# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
# list factors
f1 = 3
f2 = 5
for x in range(1, 1000):
    if x % f1 == x % f2 == 0:
        total += x
    elif x % f1 == 0:
        total += x
    elif x % f2 == 0:
        total += x

print(str(total))
