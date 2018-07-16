# Uses National Data on the relative frequency of given names
# in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt
# with xxxx (the year of birth)
# ranging from 1880 to 2013.
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by Eric Martin for COMP9021


import os
from sys import exit


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

tallies = {'F': {}, 'M': {}}
records = {'F': {}, 'M': {}}
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3: 7])
    with open(directory + '/' + filename) as file:
        for sex in {'F', 'M'}:
            tallies[sex][year] = 0           
        for line in file:
            name, sex, count = line.split(',')
            count = int(count)
            tallies[sex][year] += count
            if name == first_name:
                records[sex][year] = count
frequencies = dict.fromkeys('M', 'F')
for sex in {'F', 'M'}:
    frequencies[sex] = [(records[sex][year] * 100 / tallies[sex][year], year) for year in records[sex]]

    frequencies[sex].sort(reverse = True)
if frequencies['F']:
    min_female_frequency, female_first_year = frequencies['F'][0][0], frequencies['F'][0][1]
if frequencies['M']:
    min_male_frequency, male_first_year = frequencies['M'][0][0], frequencies['M'][0][1]
if not female_first_year:
    print('In all years, {:} was never given as a female name.'.format(first_name))
else:
    print('In terms of frequency, {:} was the most popular '
          'as a female name first in the year {:}.\n'
          '  It then accounted for {:.2f}% of all female names'.
          format(first_name, female_first_year, min_female_frequency))
if not male_first_year:
    print('In all years, {:} was never given as a male name.'.format(first_name))
else:
    print('In terms of frequency, {:} was the most popular '
          'as a male name first in the year {:}.\n'
          '  It then accounted for {:.2f}% of all male names'.
          format(first_name, male_first_year, min_male_frequency))

