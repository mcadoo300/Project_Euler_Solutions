import time

# get the start time
st = time.time()

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
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')