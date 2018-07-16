import sys
import os
directory1='female'
directory2='male'
name=input('Enter a first name:')
fname={}
mname={}
fre={}
frequency=0.0
allf=0
alln=0
j1=1
for filename in os.listdir(directory1):
    if not filename.endswith('.txt'):
        continue
    with open(directory1 + '/' + filename) as file:
        year=filename[3:7]
        ally=0
        for line in file:
            name_f,nub=line.split(',')
            nub=int(nub)
            allf=allf+nub
            ally+=nub
            if name_f==name:
                fname[year]=nub
                nubn=nub
                alln=alln+nub
        frequency=round(nubn/ally,4)
        if frequency not in fre:
            fre[frequency]=year
        
if alln==0:
    print('In all years,',name,'was never given as a female name.')
else:
    firstyear=fre[max(fre)]
    print('In terms of frequency,',name,'was the most popular as a female name first in the year',firstyear,'.')
    print(' It then accounted for {}% of all female names'.format(max(fre)*100))
                
        

        

