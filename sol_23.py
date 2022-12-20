# divisor_sum
import sol_21


def is_abundant(x):
    return x < sol_21.divisor_sum(x)


abd_list = []
for i in range(2, 28123):
    if is_abundant(i):
        abd_list.append(i)

upper_bound = 28123
sum_list = [False]*28124
x = 0
sum_test = 0
while x < len(abd_list): #abd_list of all abundant numbers <= 28123
    k = x
    while k < len(abd_list):
        n = abd_list[x] + abd_list[k]
        if n <= upper_bound:
            #sum_list[n] = True
            sum_test += n #sum all possible abundant numbers <= 28123
        k += 1
    x += 1

total_sum = 0
for i in range(28124):
#    if not sum_list[i]:
    total_sum += i
total_sum -= sum_test
print(total_sum)
