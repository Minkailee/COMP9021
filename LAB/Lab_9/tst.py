import sys
banknotes=[]
while True:
    line=input()
    if ':' not in line:
        break
    value,num=line.split(':')
    banknotes.append((int(value),int(num)))
banknotes=sorted(banknotes,key=lambda t:t[0])
banknotes.reverse()
try:
    amount=int(input('Input the desired amount:'))
    if amount<0:
        raise ValueError
except ValueError:
    print('Incorrect input!')
    sys.exit()
#print(banknotes)
minisol=[[0,[]]]+[[float('inf'),[]] for i in range(amount)]
#print(minisol)
for subvalue in range(1,amount+1):
    for i in range(len(banknotes)):
        value=banknotes[i][0]
        if subvalue<value:
            continue
        if subvalue==value:
            minisol[subvalue]=[1,[{value:1}]]
            break
        if minisol[subvalue-value][0]>=minisol[subvalue][0]:
            continue
        for option in minisol[subvalue-value][1]:
            if value not in option or option[value]<banknotes[i][1]:
                if minisol[subvalue-value][0]+1<minisol[subvalue][0]:
                    minisol[subvalue][0]=minisol[subvalue-value][0]+1
                    minisol[subvalue][1].clear()
                extendoption=dict(option)
                if value not in option:
                    extendoption[value]=1
                else:
                    extendoption[value]+=1
            if extendoption not in minisol[subvalue][1]:
                minisol[subvalue][1].append(extendoption)
mini=minisol[amount][0]
if mini==float('inf'):
    print('NO')
else:
    print(mini)
            
    
    
