import textblob
import csv


def gen_1st_n_tri_nums(n):
    tri_nums = []
    for i in range(1, n + 1):
        new_num = (i / 2) * (i + 1)
        tri_nums.append(new_num)
    return tri_nums


tri_nums = gen_1st_n_tri_nums(1000)


def get_word_val(word):
    word = word.casefold()
    word_sum = 0
    for char in word:
        key_val = ord(char)
        # shift ascii code to alphabetical pos
        key_val -= 96
        word_sum += key_val
    return word_sum


def is_triangle_num(x):
    for a in tri_nums:
        if a == x:
            return True
        if a > x:
            return False
    return False


def is_triangle_word(word):
    word_val = get_word_val(word)
    if is_triangle_num(word_val):
        return True
    return False


def run_solution():
    f = open(r"C:\Users\Mcado\OneDrive\Desktop\p042_words.txt", "r+")
    elements_list = f.readlines()
    f.close()
    list1 = elements_list[0].rsplit(",")
    list2 = []
    for v in list1:
        v = v[1:len(v) - 1]

    for v in list1:
        v = v[1:len(v) - 1]
        list2.append(v)

    count = 0
    for elem in list2:
        if is_triangle_word(elem):
            count += 1

    print(count)


# run_solution()
