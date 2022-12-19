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