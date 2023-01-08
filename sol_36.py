def reverse_string(text):
    new_text = text[::-1]
    return new_text


def is_palindrome(number):
    str_original = str(number)
    str_reverse = reverse_string(str_original)

    if str_reverse == str_original:
        return True
    return False


total_sum = 0
for i in range(1000000):
    binary = bin(i)
    binary = binary[2:len(binary)]

    if is_palindrome(i):
        if is_palindrome(binary):
            total_sum += i
print(total_sum)
