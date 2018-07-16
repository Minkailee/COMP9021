import sys
ID=input('Which data file do you want to use?')
try:
    file=open(ID)
    shape=[]
    for line in file:
        l=line.split()
        for item in l:
            shape.append(int(item))
    #print(shape)
    file.close()
    if shape==[]:
        raise ValueError
except ValueError:
    print('Incorrect input, exiting!')
    sys.exit()
except IOError:
    print('Incorrect input, exiting!')
    sys.exit()

nub= int(input('How many decilitres of water do you want to pour down?'))
try:
    if nub<0:
        raise ValueError
except ValueError:
    print('Incorrect input, exiting!')
    sys.exit()

shape=sorted(shape)
L_inorder=shape
L_set=sorted(set(shape))
#print(L_set)
height=[0]*(max(L_set)+1)
for i in L_inorder:
    height[i]+=1
L_each=[0]*(max(L_set)+1)
each=0
L_count=set(shape)
max(L_count)
L_count.remove(max(L_count))
for j in L_count:
    for y in L_set:
        if y>j:
            break
    each=(each+height[j])*(y-j)
    L_each[j]=each
#print(L_each)
v=0
#print(L_set)
for k in L_each:
    v=v+k
    if k!=0:
        L_each1=L_each
        L_each1[max(L_set)]=max(L_each)+height[max(L_set)]
        for x in L_each1:
                if x>k:
                    mark=int(L_each1.index(x))
                    gap=mark-int(L_each.index(k))
                    break
        if nub<=v and nub>v-k:
            #print(v,mark,k,gap)
            square=k/gap
            altitude=mark-(v-nub)/square
            print('The water rises to','{:.2f}'.format(altitude),'centimeters.')
            break
if nub>v:
    altitude=(nub-v)/(max(L_each)+height[max(L_set)])+max(L_set)
    print('The water rises to','{:.2f}'.format(altitude),'centimeters.')

    
    
