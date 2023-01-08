import prime_time


# return a reduced fraction

def reduce_fraction(numerator, denominator):

    num_p_f = prime_time.prime_factorization(numerator)
    denom_p_f = prime_time.prime_factorization(denominator)

    common_factors = [[], []]

    if len(num_p_f) > len(denom_p_f):
        for factor in range(len(num_p_f[0])):
            for f in range(len(denom_p_f[0])):
                if denom_p_f[0][f] == num_p_f[0][factor]:
                    common_factors[0].append(num_p_f[0][factor])
                    common_factors[1].append(min(num_p_f[1][f], denom_p_f[1][factor]))
    else:
        for factor in range(len(denom_p_f[0])):
            for f in range(len(num_p_f[0])):
                if num_p_f[0][f] == denom_p_f[0][factor]:
                    common_factors[0].append(num_p_f[0][f])
                    common_factors[1].append(min(num_p_f[1][f], denom_p_f[1][factor]))

    gcd = 1
    for f in range(len(common_factors[0])):
        gcd *= common_factors[0][f]**common_factors[1][f]
    numerator /= gcd
    denominator /= gcd

    return [numerator, denominator]


def reduce_check(a, b, x, y):
    if b == 0:
        return False
    numerator = 10*a + b
    denom = 10*x + y

    reduced_fraction = reduce_fraction(numerator, denom)

    if a % reduced_fraction[0] == 0:
        c1 = a / reduced_fraction[0]
        if y == b:
            if c1*reduced_fraction[1] == x:
                return True
        elif x == b:
            if c1*reduced_fraction[1] == y:
                return True
    if b % reduced_fraction[0] == 0:
        c1 = b / reduced_fraction[0]
        if y == b:
            if c1*reduced_fraction[1] == x:
                return True
            elif c1*reduced_fraction[1] == y:
                return True

    return False

# """
fraction_list = []

# loop through first digit check
for a in range(1, 10):
    for b in range(1, 10):
        for x in range(a,10):
            for y in range(1, 10):
                num = a * 10 + b
                denom = x * 10 + y
                if num/denom < 1:
                    if reduce_check(a, b, x, y):
                        fraction_list.append(reduce_fraction(num, denom))
# """

print(fraction_list)
