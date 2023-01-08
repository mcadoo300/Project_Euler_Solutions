import math
import time

start = time.time()


def is_pent(p):
    if (math.sqrt((p * 24) + 1) + 1) % 6 == 0:
        return True
    return False


def is_hex(h):
    if (math.sqrt((8*h)+1) + 1) % 4 == 0:
        return True
    return False


i = 286

flag1 = True
while flag1:
    new_num = (i*(i+1))/2
    if is_pent(new_num) and is_hex(new_num):
        print(new_num)
        break
    i += 1

