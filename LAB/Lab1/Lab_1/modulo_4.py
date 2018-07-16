# Prompts the user for a strictly positive integer N,
# generates a list of N random integers between 0 and 99, prints out the list,
# computes the number of elements equal to 0, 1, 2 3 modulo 4, and prints those out.
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

L = [randint(0, 99) for _ in range(nb_of_elements)]
print('The list is:' , L)
# - remainders_modulo_4[0] to record the number of elements equal to 0 modulo 4,
# - remainders_modulo_4[1] to record the number of elements equal to 1 modulo 4,
# - remainders_modulo_4[2] to record the number of elements equal to 2 modulo 4,
# - remainders_modulo_4[3] to record the number of elements equal to 3 modulo 4.
remainders_modulo_4 = [0] * 4
for i in range(nb_of_elements):
    remainders_modulo_4[L[i] % 4] += 1
for i in range(4):
    if remainders_modulo_4[i] < 2:
        print(' There is {} element equal to {} modulo 4.'.format(remainders_modulo_4[i], i))
    else:
        print(' There are {} elements equal to {} modulo 4.'.format(remainders_modulo_4[i], i))
