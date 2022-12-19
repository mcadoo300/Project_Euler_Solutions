#problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#each number can be written as a product of primes
#determine the prime factors of x by checking if: prime % x ==0
#return largest prime
def largest_prime(x):
    prime_factors = [1]
    if x % 2 == 0: #2 is the only even prime number so check first
        prime_factors.append(2)
        while x % 2 == 0:
            x /= 2

    prime_factor = 3 #set to 3
    while x != 1:
        if x % prime_factor == 0: #factor out each prime
            prime_factors.append(prime_factor)
            x /= prime_factor
        else:
            prime_factor+=2#go to next odd number
    return prime_factors.pop(len(prime_factors)-1)


print(largest_prime(600851475143))