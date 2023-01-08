import prime_time
# for is_pan
# requires modified digits in sol_32 to 1,2,3,4,5,6,7
import sol_32

primes_list = prime_time.list_primes_under(7654322)

primes_list.reverse()

for x in primes_list:
    if sol_32.is_pan(str(x)):
        print(x)
        break
