import textblob

tower = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
new_tower = ""
for x in tower:
    new_tower += str(x.replace("\n", " "))
# number of elements in tower
cardinality = ((len(new_tower) - (len(new_tower) + 1) / 3) + 1) / 2
number_list = [[0] * 15 for _ in range(15)]
i = 0
j = 0
count = 0
while count < cardinality:
    str_val = new_tower[(count * 2) + count:(count * 2) + 2 + count]
    if i >= j:
        number_list[i][j] = int(str_val)
        j += 1
    else:
        j = 0
        i += 1
        number_list[i][j] = int(str_val)
        j += 1
    count += 1


def sum_count(i, j, tree, sum1):
    if i == 14:
        sum1 += tree[i][j]
        return sum1
    else:
        sum_left = sum_count(i + 1, j, tree, sum1)
        sum_right = sum_count(i + 1, j + 1, tree, sum1)
        if sum_left > sum_right:
            sum_left += tree[i][j]
            return sum_left
        else:
            sum_right += tree[i][j]
            return sum_right


print(sum_count(0, 0, number_list, 0))
