import itertools
number=input('Input a number that we will use as available digits:')
desire=int(input('Input a number that represents the desired sum:'))
Lnub=[]
for x in number:
    Lnub.append(int(x))
#print(Lnub)
Lcom=[]
for i in range(1,len(Lnub)+1):
    Liter=itertools.combinations(Lnub,i)
    Lcom.append(list(Liter))
#print(Lcom)
n=0
for L in Lcom:
    for com in L:
        if sum(com)==desire:
            n=n+1
if n==1:
    print('There is a unique solution.')
elif n==0:
    print('There is no solution.')
else:
    print('There are',n,'solutions.')
