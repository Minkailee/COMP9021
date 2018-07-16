for i in range(99,1000):
    L=[0]
    for j in range(1,i//2+1):
        if i%j==0:
            L.insert(0,j)
    sum=0
    for x in L:
        sum=sum+x
    if sum==i:
        print(i, 'is a 3-digit perfect number.')
