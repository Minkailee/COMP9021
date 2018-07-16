# Implements coding and decoding functions for pairs of integers.
# For coding, start at point (0, 0), move to point (1, 0), and turn
# around in an anticlockwise manner.
# 定圈法
# Written by Minkai Li(z5095946) for COMP9021



from math import sqrt


def encode(a, b):
    n=0
    if abs(a)>=abs(b):
       n=abs(a)
    else:
       n=abs(b)
    Lx=[n]
    Ly=[1-n]
    if n==0:
        print('0')
    else:
        nub1=(n*2-1)*(n*2-1)
        if Lx[0]==a and Ly[0]==b:
            return(int(nub1))
        elif a==n and b!=-n:
            return(int(nub1+b+n-1))
        elif b==n and a!=n:
            return(int(nub1+3*n-a-1))
        elif a==-n and b!=n:
            return(int(nub1+5*n-b-1))
        elif b==-n and a!=-n:
            return(int(nub1+7*n+a-1))
    
def decode(nub):
    n=0
    while True:
        if sqrt(nub)>=2*n-1 and sqrt(nub)<2*n+1:
            break
        n=n+1
    Lx=[n]
    Ly=[1-n]
    if n==0:
        Ly=[0]
        print('('+str(Lx[0])+',',str(Ly[0])+')')
    else:
        nub1=(n*2-1)*(n*2-1)
        if nub-nub1<=2*n-1:
            a=int(n)
            b=int(Ly[0]+nub-nub1)
            t=(a,b)
            return(t)
        elif nub-nub1<=4*n-1:
            b=int(n)
            a=int(Lx[0]-(nub-nub1-2*n+1))
            t=(a,b)
            return(t)
        elif nub-nub1<=6*n-1:
            a=int(-n)
            b=int(n-(nub-nub1-4*n+1))
            t=(a,b)
            return(t)
        elif nub-nub1<=8*n-1:
            b=int(-n)
            a=int(-n+nub-(nub1+6*n-1))
            t=(a,b)
            return(t)
    

