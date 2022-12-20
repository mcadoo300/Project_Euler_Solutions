# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

flag = False

i=1
x=1
while not flag:
    while x < 21:
        if i % x != 0:
            x = 21
        if x == 20:
            flag = True
        x +=1
    i += 1
    x = 1
print(i-1)