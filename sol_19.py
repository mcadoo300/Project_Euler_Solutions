def days_in_month(x, y):
    # feb
    if is_leap_year(y):
        if x == 2:
            return 29

    if x == 2:
        return 28

    month_30 = [3, 5, 8, 10]
    for m in month_30:
        if x == m:
            return 30
    return 31


def is_leap_year(y):
    is_century = (y % 1000) - y
    if is_century % 100 == 0:
        if y % 400 == 0:
            return True
        return False
    if y % 4 == 0:
        return True
    return False


year = 1900
month = 0
week_day_pos = 1

count = 0
while year < 2001:
    while month < 12:
        week_day_pos += days_in_month(month, year) - 28
        week_day_pos = week_day_pos % 7
        if week_day_pos == 6:
            count += 1
        month += 1
    year += 1
    month = 0

# subtract the two from the year 1900
print(count-2)
