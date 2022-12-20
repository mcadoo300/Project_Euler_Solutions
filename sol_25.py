total = 0
fibNew = 1
fibPrev = 1
k=2

while fibNew % 10**999 == fibNew:
    fibNum = fibPrev + fibNew
    fibPrev = fibNew
    fibNew = fibNum
    k += 1
print(k)