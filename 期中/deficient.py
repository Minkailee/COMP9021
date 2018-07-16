import sys
try:
    s=input('Enter two strictly positive numbers:')
    a,b=s.split(' ')
    a=int(a)
    b=int(b)
    if a<=0 or b<=0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
min_=min(a,b)
max_=max(a,b)
if min_==1:
    L=[1]
else:
    L=[]
for i in range(min_,max_+1):
    sum_=0
    if i==1:
        continue
    for j in range(1,i):
        if (i/j)%1==0:
            sum_=sum_+j
    if sum_<i:
        L.append(i)
print(L)
if a<=b:
    start=[L[0]]
else:
    start=[L[-1]]
end=[]
if int(len(L))==1:
    end.append(L[0])
else:
    if a<=b:
        for i in range(0,int(len(L))-1):
            if L[i]+1==L[i+1]:
                if i+1==int(len(L))-1:
                    end.append(L[i+1])
                continue
            else:
                start.append(L[i+1])
                end.append(L[i])
            if i+1==int(len(L))-1:
                end.append(L[i+1])
    else:
        for i in range(int(len(L))-1,0,-1):
            if L[i]-1==L[i-1]:
                if i-1==0:
                   end.append(L[i-1]) 
                continue
            else:
                start.append(L[i-1])
                end.append(L[i])
            if i-1==0:
                end.append(L[i-1])
print(start)
print(end)
length=[abs(end[i]-start[i]) for i in range(0,int(len(end)))]
#print(length)
index=length.index(max(length))
print('The longest sequence of deficient numbers between {} and {} ranges between {} and {}.'.format(a,b,start[index],end[index]))
