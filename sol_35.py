import prime_time

prime_list = prime_time.list_primes_under(1000000)


def is_circular(x):
    string_copy = str(x)
    char_list = []
    for a in string_copy:
        char_list.append(a)

    if len(char_list) == 1:
        return True
    i = 0

    while i < len(char_list):
        new_prime_string = ""
        for a in char_list:
            new_prime_string += str(a)

        new_prime = int(new_prime_string)
        if not prime_time.is_prime(new_prime):
            return False
        char_list.append(char_list[0])
        char_list.remove(char_list[0])
        i += 1
    return True


count = 0
for prime_num in prime_list:
    if is_circular(prime_num):
        count += 1

print(count)

