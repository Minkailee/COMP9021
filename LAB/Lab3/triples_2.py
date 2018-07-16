from math import sqrt
L=[0]*1000
Ls=['0']*1000
for i in range(100,1000):
    for a in range(0,round(sqrt(i))):
        b=sqrt((i-a*a))
        if b%1==0:
            s=str(a)+'^2+'+str(int(b))+'^2'
            Ls[i]=s
            L[i]=1
            #print(str(i)+'=',Ls[i])
            break
for j in range(100,998):
    if L[j]==1 and L[j+1]==1 and L[j+2]==1:
        s1='('+str(j)+', '+str(j+1)+', '+str(j+2)+')'
        s2='('+Ls[j]+', '+Ls[j+1]+', '+Ls[j+2]+')'
        print(s1,'(equal to '+s2+') is a solution.')
