Lall=[]
newLall=[]
for i in range(10,99):
    for j in range(10,99):
        for k in range(10,99):
            a=str(i)+str(j)+str(k)
            p=str(i*j*k)
            La=[]
            Lp=[]
            for x in a:
                La.append(int(x))
            for y in p:
                Lp.append(int(y))    
                La=sorted(La)
                Lp=sorted(Lp)
            if La==Lp:
                sall=''
                L=[i,j,k]
                Ls1=[]
                Ls2=[]
                s=str(i)+str(j)+str(k)
                for id in s:
                    Ls1.append(int(id))
                    if int(id) not in Ls2:
                        Ls2.append(int(id))
                if Ls1==Ls2:
                    Ls=sorted(L)
                    Lall.append(Ls)
                    for id in Lall:
                        if id not in newLall:
                            newLall.append(L)
                        
for element in newLall:
    e0=element[0]
    e1=element[1]
    e2=element[2]
    e=e1*e2*e0
    print(str(e0),'x',str(e1),'x',str(e2),'=',str(e),'is a solution.')
