# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx--xxxx, and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the second year can be anterior to the first year.
# - The month is a two digit number.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv


filename = 'monthly.csv'
if not os.path.exists(filename):
    print('There is no file named {} in the working directory, giving up...'.format(filename))
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
range_for_the_years = input('Enter a range for the years in the form XXXX--XXXX: ')
month = input('Enter a month in the form of a 2-digit number: ')
sumall=0
average = 0
years_above_average = []
start,end=range_for_the_years.split('--')
start=int(start)
end=int(end)
if start>end:
    transform=start
    start=end
    end=transform
if month[0]=='0':
    month=int(month[1])
else:
    month=int(month)
GCAG={}
GISTEMP={}
with open(filename) as csvfile:
    judge1=0
    judge2=0
    for line in csvfile:
        form,date,mean=line.split(',')
        if form=='GCAG':
            year,mon=date.split('-')
            year=int(year)
            if judge1!=year:
                GCAG[year]=[0.0]*13
                judge1=year  
            if mon[0]=='0':
                mon=(int(mon[1]))
            else:
                mon=(int(mon))
            mean=float(mean)
            GCAG[year][mon]=mean
        if form=='GISTEMP':
            year,mon=date.split('-')
            year=int(year)
            if judge2!=year:
                GISTEMP[year]=[0.0]*13
                judge2=year  
            if mon[0]=='0':
                mon=(int(mon[1]))
            else:
                mon=(int(mon))
            mean=float(mean)
            GISTEMP[year][mon]=mean
amount=0
if source=='GCAG':
    for key in GCAG:
        if key <= end and key >= start:
            sumall=sumall+GCAG[key][month]
            amount=amount+1
    average=float(sumall/amount)
    for key in GCAG:
        if GCAG[key][month] > average and (key <= end and key >= start):
            years_above_average.append(key)
if source=='GISTEMP':
    for key in GCAG:
        if key <= end and key >= start:
            sumall=sumall+GISTEMP[key][month]
            amount=amount+1
    average=float(sumall/amount)
    for key in GISTEMP:
        if GISTEMP[key][month] > average and (key <= end and key >= start):
            years_above_average.append(key)
            
    

print('The average anomaly for this month of those years is: {:.2f}.'.format(average))
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
