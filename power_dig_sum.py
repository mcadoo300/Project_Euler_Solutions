#problem 16
#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?


k = 2**1000

stringVal = str(k)

sum_dig = 0

for x in stringVal:
    sum_dig = sum_dig + int(x)

print(sum_dig)
