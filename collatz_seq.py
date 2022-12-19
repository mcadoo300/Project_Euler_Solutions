import math

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


maxSeq=0
for x in range(1,1000000):
    if get_sequence_len(x) > maxSeq :
        maxSeq=get_sequence_len(x)
        print(x)

print(maxSeq)