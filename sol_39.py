import math


def get_perim(x,y,z):
    sum1 = x
    sum1 += y
    sum1 += z
    return sum1


p = 3
count = 0
max_p = 0
max_count = 0
while p <= 1000:
    for a in range(1, p):
        for b in range(1, p-a):
            c = math.sqrt((a**2 + b**2))
            if get_perim(a,b,c) == p:
                count += 1
    count /= 2
    if count > max_count:
        max_count = count
        max_p = p
    p += 1
    count = 0


print(max_p)

