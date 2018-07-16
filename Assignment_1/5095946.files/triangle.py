import sys
ID=input('Which data file do you want to use?')
try:
    file=open(ID)
    Lall=[]
    countl=0
    for line in file:
        countl=countl+1
        l=line
        l1=l.split()
        Leach=[]
        for item in l1:
            Leach.append(int(item))
        Lall.append(Leach)
    #print(Lall)
    file.close()
    if Lall==[]:
        raise ValueError
except ValueError:
    print('Incorrect input, exiting!')
    sys.exit()
except IOError:
    print('Incorrect input, exiting!')
    sys.exit()
Lsum=[]
Lroute=[]
for i in range(2**(countl-1)):
    s=str(bin(i).replace('0b',''))
    route=[] 
    for item in s:
        route.append(int(item))
    while len(route)<countl-1:
        route.insert(0,0)
    Lroute.append(route)
    #print(route)
    sum1=0
    level=0
    conor=0
    for item in route:
        sum1=sum1+(Lall[level][conor])
        if item==0:
           conor=conor 
        else:
            conor=conor+1
        level=level+1
    sum1=sum1+(Lall[level][conor])
    #print(sum1)
    Lsum.append(sum1)
nub=0
Lnub=[]
for item in Lsum:
    if item == max(Lsum):
        nub=nub+1
        Lnub.append(Lsum.index(item))
Left=[]
for x in Lnub:
    Left.append(sum(Lroute[x]))
Best=Lnub[Left.index(min(Left))]
level=0
conor=0
bestroute=[]
for item in Lroute[Best]:
        bestroute.append(Lall[level][conor])
        if item==0:
           conor=conor 
        else:
            conor=conor+1
        level=level+1
bestroute.append(Lall[level][conor])
print('The largest sum is:',max(Lsum))
print('The number of paths yielding this sum is:',nub)
print('The leftmost path yielding this sum is:',bestroute)
        
    
    
        
    
    
       
