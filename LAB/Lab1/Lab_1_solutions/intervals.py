# Prompts the user for a strictly positive integer N,
# generates a list of N random integers between 0 and 19, prints out the list,
# computes the number of elements strictly less 5, 10, 15 and 20, and prints those out.
#
# Written by Eric Martin for COMP9021


from random import randint
import sys


nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
    
L = [randint(0, 19) for _ in range(nb_of_elements)]
print('The list is:' , L)
# - intervals[0] to record the number of elements between 0 and 4,
#   that is, elements e such that e // 5 == 0
# - intervals[1] to record the number of elements between 5 and 9
#   that is, elements e such that e // 5 == 1
# - intervals[2] to record the number of elements between 10 and 14
#   that is, elements e such that e // 5 == 2
# - intervals[3] to record the number of elements between 15 and 19
#   that is, elements e such that e // 5 == 3
intervals = [0] * 4
for i in range(nb_of_elements):
    intervals[L[i] // 5] += 1
for i in range(4):
    if intervals[i] < 2:
        print(' There is {} element between {} and {}.'.format(intervals[i], 5 * i, 5 * i + 4))
    else:
        print(' There are {} elements between {} and {}.'.format(intervals[i], 5 * i, 5 * i + 4))
