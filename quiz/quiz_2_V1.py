# Implements coding and decoding functions for pairs of integers.
# For coding, start at point (0, 0), move to point (1, 0), and turn
# around in an anticlockwise manner.
# 遍历法
# Written by Minkai Li(z5095946) for COMP9021


from math import sqrt


def encode(a, b):
    Lx=[0]
    Ly=[0]
    n=1
    nub=1
    p_or_n=1
    while True:
        for i in range(1,n+1):
            if Lx[nub-1]==a and Ly[nub-1]==b:
                break   
            Lx.append(Lx[nub-1]+p_or_n)
            Ly.append(Ly[nub-1])
            nub=nub+1       
        for j in range(1,n+1):
            if Lx[nub-1]==a and Ly[nub-1]==b:
                break  
            Ly.append(Ly[nub-1]+p_or_n)
            Lx.append(Lx[nub-1])
            nub=nub+1
        if Lx[nub-1]==a and Ly[nub-1]==b:
            print(nub-1)
            break 
        p_or_n=p_or_n*(-1)
        n=n+1

    
def decode(k):
    Lx=[0]
    Ly=[0]
    n=1
    nub=1
    p_or_n=1
    while True:
        for i in range(1,n+1):
            if nub-1==k:
                break   
            Lx.append(Lx[nub-1]+p_or_n)
            Ly.append(Ly[nub-1])
            nub=nub+1       
        for j in range(1,n+1):
            if nub-1==k:
                break   
            Ly.append(Ly[nub-1]+p_or_n)
            Lx.append(Lx[nub-1])
            nub=nub+1
        if nub-1==k:
            print('('+str(Lx[nub-1])+',',str(Ly[nub-1])+')')
            break   
        p_or_n=p_or_n*(-1)
        n=n+1

    

