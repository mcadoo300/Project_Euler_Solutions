import math

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


word_sum = 0
x = [900]
for i in range(1, 1000):
    if i < 10:
        word_sum += len(ones[i])
    elif i < 20:
        index_teen = i % 10
        word_sum += len(teens[index_teen])
    elif i < 100:
        index_tens = math.floor(i/10)
        index_ones = i % 10
        word_sum += len(tens[index_tens])
        if index_ones != 0:
            word_sum += len(ones[index_ones])
    elif i < 1000:
        index_hund = math.floor(i/100)
        word_sum += len(ones[index_hund])
        teen_check = i % 100
        if teen_check == 0:
            word_sum += 7
            pass
        elif teen_check < 10:
            # for "hundred" "and"
            word_sum += 7
            word_sum += 3
            word_sum += len(ones[teen_check])
        elif teen_check < 20:
            word_sum += 7
            word_sum += 3
            word_sum += len(teens[teen_check % 10])
        elif teen_check < 100:
            word_sum += 7
            word_sum += 3
            index_tens = math.floor(teen_check / 10)
            index_ones = teen_check % 10
            word_sum += len(tens[index_tens])
            if index_ones != 0:
                word_sum += len(ones[index_ones])

word_sum += len("onethousand")

print(word_sum)