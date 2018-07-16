import sys
import math
import copy
ID=input('Which data file do you want to use?')
try:
    file=open(ID)
    town=[]
    fish=[]
    for line in file:
        l=line.split()
        town.append(int(l[0]))
        fish.append(int(l[1]))
    #print(town,fish)
    file.close()
    if town==[] or fish==[]:
        raise ValueError
except ValueError:
    print('Incorrect input, exiting!')
    sys.exit()
except IOError:
    print('Incorrect input, exiting!')
    sys.exit()

average=int(sum(fish)/len(fish))
mini=int(min(fish))
answer=[]
for i in range(mini,average):
    fish1=copy.deepcopy(fish)
    for j in range(len(town)-1):
        if fish1[j]-i<0:
            fish1[j+1]=fish1[j+1]-(town[j+1]-town[j])-abs(fish1[j]-i)
        if fish1[j]-i>=0:
            if fish1[j]<=town[j+1]-town[j]:
                pass
            else:
                fish1[j+1]=fish1[j+1]+fish1[j]-i-(town[j+1]-town[j])
    if fish1[-1]<i:
        break
    if fish1[-1]>=i:
        answer.append(i)
print('The maximum quantity of fish that each town can have is',str(answer[-1])+'.')
        
        
    

