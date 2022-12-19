#problem 26
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.



#will return the repeating sequence of a digit 1/x
#if 1/x is not repeating this function return -1
def get_sequence(x):
    new_dig=1%x
    seq=[new_dig]
    while new_dig!=0:
        new_dig=(new_dig*10)%x#remainder after each long division cycle
        for y in range(len(seq)):
            pos=len(seq)-1-y
            if(seq[pos]==new_dig):#if the remainder has appeared before the sequence is repeating
                return len(seq)-pos

        seq.append(new_dig)

    return -1

#find the largest repeating decimal in the range of:
#1/2 , ... , 1/999
n = 999
flag = False
maxRep = 0
while not flag:
    if get_sequence(n) > maxRep:
        maxRep = get_sequence(n)
        #for each n there are n-1 possible remainders(if the remainder is 0 its not repeating)
        #so when the sequence is larger than the next element in the loop we have our max repeating decimal
        if maxRep >= (n-1):
            flag = True

    n -= 1

print(n+1)
#983
