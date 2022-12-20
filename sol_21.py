# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
import prime_time

def get_divisors(x):
    divisors=[]
    for y in range(1, (x // 2)+1):
        if x % y == 0:
            divisors.append(y)
    return divisors


# updated function method
def divisor_sum(x):
    factors = prime_time.prime_factorization(x)
    product = []
    count = 0
    for y in factors[0]:
        term = y**(factors[1][count]+1) - 1
        product.append(term/(y-1))
        count += 1

    total_product =1
    for y in product:
        total_product *= y

    return total_product-x


#total_sum = 0
#for a in range(2, 10000):
#    k = divisor_sum(a)
#    if k != a:
#        if a == divisor_sum(k):
#            total_sum += (a+k)
#print(total_sum/2)


# OLD FUNCTION METHOD #
# list1 = get_divisors(x)
# sum_total = 0
# for x in list1:
#    sum_total += x
# return sum_total