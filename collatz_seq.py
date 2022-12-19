
#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.


def next_term(x):
    if (x%2) == 0:
        return x/2
    else:
        return 1+3*x


def get_sequence_len(x):
    seq=[x]
    i=0
    while next_term(seq[i]) != 1:
        seq.append(next_term(seq[i]))
        i+=1

    return len(seq) + 1


maxSeq = 0
for x in range(1,1000000):
    if get_sequence_len(x) > maxSeq :
        maxSeq=get_sequence_len(x)
        print(x)

print(maxSeq)