import prime_time

primes_list = prime_time.list_primes_under(1000000)


# create function to determine if sum of primes
def is_sum_of_primes(x):
    if x % 10 == x:
        return []
    list1 = prime_time.list_primes_under(x)
    sum_list =[]
    list1.reverse()
    try_count = 0
    flag = True
    while flag:
        i = 0
        new_num = x
        while new_num > 0 and (try_count + i) <= (len(list1) - 1):
            new_num -= list1[try_count + i]
            sum_list.append(list1[try_count + i])
            i += 1
        if new_num == 0:
            return sum_list
        if new_num > 0:
            flag = False
        try_count += 1
        sum_list = []
    return sum_list



k = 0
final_sum = 0

while final_sum < 1000000:
    final_sum += primes_list[k]


print(longest_list)