import prime_time
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

list_primes = prime_time.list_primes_under(2000000)
sum_total = 0
for x in list_primes:
    sum_total += x
print(sum_total)
