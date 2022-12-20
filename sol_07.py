# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import prime_time

count = 1
x=3
while count < 10001:
    if prime_time.is_prime(x):
        count += 1
    if count != 10001:
        x += 2
print(x)
