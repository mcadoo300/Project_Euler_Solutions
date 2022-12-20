x = 100
total = 1
while x >1:
    total *= x
    x -= 1
str_val = str(total)
sum_total = 0
for x in str_val:
    sum_total += int(x)

print(sum_total)