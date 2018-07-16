import sys
s=input('Please input a string of lowercase letters:')
if not all(c.islower() for c in s):
    print('Incorrect input.')
    sys.exit()
L=[]
for x in s:
    L.append(ord(x))
#print(L)
L2=[]
for i in range(0,len(L)):
    c=L[i]
    L1=[]
    for j in range(i,len(L)):
        if L[j]==c:
            L1.append(L[j])
            c=c+1
    L2.append(L1)
L2.reverse()
L2=sorted(L2,key=lambda t:len(t))
print('The solution is: ',end='')
for x in L2[-1]:
    print(chr(x),end='')
        
