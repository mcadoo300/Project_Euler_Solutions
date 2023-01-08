import prime_time

prime_list = prime_time.list_first_n_primes(100000)
prime_list.remove(2)
prime_list.remove(3)
prime_list.remove(5)
prime_list.remove(7)


def is_trunctable(number):
    str_val = str(number)
    for i in range(len(str_val) - 1):
        z = int(str_val[i + 1:len(str_val)])
        if not prime_time.is_prime(z):
            return False
        z = int(str_val[0:len(str_val) - 1 - i])
        if not prime_time.is_prime(z):
            return False
    return True


count = 0
total_sum = 0
for number in prime_list:
    if is_trunctable(number):
        count += 1
        total_sum += number
    if count == 11:
        break

print(total_sum)
