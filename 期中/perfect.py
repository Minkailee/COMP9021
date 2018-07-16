# Finds all perfect 3-digit numbers.
#
# Written by Eric Martin for COMP9021


for i in range(100, 1000):
    sum_of_divisors = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            sum_of_divisors += j
    if i == sum_of_divisors:
        print('{} is a 3-digit perfect number.'.format(i))
