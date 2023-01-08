import time

st = time.time()
import prime_time

global primes_list
primes_list = prime_time.list_primes_under(1000000)
print("First list count: " + str(len(primes_list)))


# the general strategy to solve this problem:
#   do a thorough sieve of primes which cannot show this property
#   once a prime has been removed, also remove members of that "family"
# note: a prime may belong to multiple families


# returns if prime is in list of primes
def is_in_list(x, list1):
    for p in range(len(list1)):
        if list1[p] == x:
            return True
        if list1[p] > x:
            break
    return False


# remove all primes less than 56004 since 56003 is a(given) lower bound
i = 0
while i < len(primes_list):
    prime = primes_list[i]
    if prime < 56004:
        primes_list.remove(prime)
    else:
        break
print("lower bound sift count: " + str(len(primes_list)))


# create function which returns number of repeating digits:
def num_repeating_digits(num1):
    str_num1 = str(num1)
    repeating_count = 0
    for digit in str_num1:
        if str_num1.count(digit) > 1:
            repeating_count += str_num1.count(digit)
            str_num1 = str_num1.replace(digit, "")
    return repeating_count


# create a function to return how many sets of repeating digits
def get_num_sets_repeating(num2):
    str_num2 = str(num2)
    set_count = 0
    for digit in str_num2:
        if str_num2.count(digit) > 1:
            set_count += 1
            k = 0
            while k < str_num2.count(digit):
                str_num2 = str_num2.replace(digit, "")
                k += 1
    return set_count


# we will first wish to rule out the family of no-repeaters
# while it is unlikely a prime with no-repeat digits will be the family we seek
# it should not take long to check
# if there are no repeating digits then there are (l-1) * 9 primes to check(per prime),
#       where l is the number of digits.
#           the first digit cant be cycled through enough numbers to create a family of 8,
#           since every other digit 1-9 is even and therefore the number ...**d can only be prime,
#           for d = 1,3,5,7,9


# get index positions of non_repeaters
def index_non_repeaters():
    index_list = []
    j = 0
    while j < len(primes_list):
        prime1 = primes_list[j]
        if get_num_sets_repeating(prime1) == 0:
            index_list.append(j)
        j += 1
    return index_list


# create specific function to test replacing single_digit
def sift_singleton(num3):
    str_num3 = str(num3)
    end3 = len(str_num3)
    for v in range(1, len(str_num3)):
        # get digits from v to end
        if v == end3:
            new_num = str_num3[v]
        new_num = str_num3[v:end3]

        # test changing digit v-1 from 1-9
        for f in range(1, 10):
            # change digit pos v
            new_num = str(f) + new_num
            # append any previous digits
            if v == 2:
                new_num = str_num3[0] + new_num
            elif v > 2:
                new_num = str_num3[0:v - 1] + new_num

            # check if new_num is prime
            # if count > 7 we have found the family
            count = 0
            if not is_in_list(int(new_num), primes_list):
                return False
            else:
                count += 1
            new_num = str_num3[v:end3]
    if count >= 8:
        return True
    return False


# point of runtime comparison:
# instead of using rc
# use .remove at 134
# ^^^ slower * time later
# eliminate non_repeaters
def preform_first_sift():
    # number of removed primes
    rc = 0
    # index positions of no_repeaters
    family_no_rep_pos = index_non_repeaters()
    sift_copy = primes_list.copy()
    flag = True
    while flag:
        for pos in family_no_rep_pos:
            if sift_singleton(primes_list[pos]):
                flag = False
                print("DONE")
                break
        if flag:
            for pos in family_no_rep_pos:
                primes_list.pop(pos - rc)
                rc += 1
            flag = False
    # first sift complete
    print("non repeating sift: " + str(len(primes_list)))


# preform_first_sift()


# from here we will create an array which stores the number of families each prime belongs to
# then increment through each prime and do the following:
#       generate family of primes by replacing n digits
#       if: the family size == 8 WE ARE DONE
#       else: decrement the family value of each member
#   remove all numbers from the list if their family value == 0


# get u x 2 matrix, where u = number of repeated digits
# col 0 is the digit which repeats
# col 1 is the number of times it repeats
def get_rep_matrix(num4):
    digit_char = [[0] * 2 for _ in range(get_num_sets_repeating(num4))]
    str_num4 = str(num4)
    repeating_count = 0
    for digit in str_num4:
        if str_num4.count(digit) > 1:
            digit_char[repeating_count][0] = int(digit)
            digit_char[repeating_count][1] = str_num4.count(digit)
            repeating_count += 1
            str_num4 = str_num4.replace(digit, "")
    return digit_char


# get number of families of number
def get_num_families(num4):
    digit_matrix = get_rep_matrix(num4)
    num_families = 0
    for row in digit_matrix:
        num_families += row[1] - 1
    return num_families


# now to generate the actual primes in each family starting from the smallest prime

# each family is generated by taking one repeating digit, say 'd', and checking if
# the number created by letting d = [1,...,9] is prime
# if it is: add it to the list

# just to stay on track, we are looking for a prime, the lowest prime, which generates 8 primes in this fashion
def repeated_digit_pos(num5):
    str_num5 = str(num5)
    digit_list = []
    for digit in str_num5:
        digit_list.append(int(digit))
    # size for position matrix is decided by the rep_matrix
    len_wid = get_rep_matrix(num5)
    # matrix to hold positions of repeated values
    position_matrix = [[0] * len_wid[_][1] for _ in range(len(len_wid))]

    # count of how many repeating values weve looked at
    count = 0
    for row in len_wid:
        digit_val = row[0]
        nr = 0
        while nr < row[1]:
            # add position
            position_matrix[count][nr] = digit_list.index(digit_val)
            digit_list.remove(digit_val)
            digit_list.insert(position_matrix[count][nr], 0)
            nr += 1
        count += 1
    # the position matrix now encodes the useful information about repeated digits
    # each list represents a set of place values we may change
    return position_matrix


# create a funciton to generate possible family members
def get_digit_replacement_list(num6):
    pos_matrix = repeated_digit_pos(num6)
    replacement_nums = [[] for _ in range(len(pos_matrix))]
    str_num6 = str(num6)
    digit_list6 = []
    for z in str_num6:
        digit_list6.append(z)
    count = 0
    for row in pos_matrix:
        for r in range(10):
            new_num = digit_list6
            for pos in row:
                if pos == 0 and r == 0:
                    break
                new_num.pop(pos)
                new_num.insert(pos, str(r))
            str_new_num = ""
            for h in new_num:
                str_new_num += str(h)
            # check for leading zeros
            replacement_nums[count].append(int(str_new_num))
        count += 1
    return replacement_nums


# get family(ies) of digit replacements and prime
def get_family(num7):
    possible_members = get_digit_replacement_list(num7)
    family_primes = [[] for _ in range(len(possible_members))]
    b = 0
    while b < len(possible_members):
        for prime in possible_members[b]:
            if is_in_list(prime, primes_list):
                family_primes[b].append(prime)
            # trim off repeats
            for s in family_primes[b]:
                while family_primes[b].count(s) > 1:
                    family_primes[b].remove(s)
        b += 1
    return family_primes


# generate array which lists number of families each prime belongs to
global family_counts
family_counts = []
for p in primes_list:
    family_counts.append(get_num_families(p))

# array of pools to track which prime we want
# each index in this tracker corresponds to a prime
# when the primes respective family counts drops to zero we turn to false
bool_tracker = [True] * len(primes_list)
finished = False
for t in range(315, len(primes_list)):
    if family_counts[t] != 0:
        family_list = get_family(primes_list[t])
        for fam in family_list:
            if len(fam) > 7:
                finished = True
                print(family_list)
                break
            else:
                for c in fam:
                    family_counts[primes_list.index(c)] -= 1
    if finished:
        break

et = time.time()

print(et - st)
