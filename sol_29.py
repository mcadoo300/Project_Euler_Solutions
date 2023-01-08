unique_num = [4]

for a in range(2, 101):
    for b in range(2, 101):
        num = a ** b
        for x in range(len(unique_num)):
            if unique_num[x] == num:
                break
            elif x == len(unique_num) - 1:
                unique_num.append(num)

print(len(unique_num))
