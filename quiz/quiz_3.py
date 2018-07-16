# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the number of blocks
# in the largest block construction, determined by rows of 1s that can be stacked
# on top of each other. 
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()


# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def size_of_largest_construction():
    Lall=[]
    for i in range(dim):
        Leach=[]
        for j in range(dim):
            Leach.append(1) if grid[i][j] else Leach.append(0)
        Lall.append(Leach)
    #for x in Lall:
        #print(x)
    Lsize=[]
    Lallp=[0]*100
    Lpoint=[]
    size=0
    for i in range(9,-1,-1):
        for j in range(0,10):
            if Lall[i][j]==1:
                for k in range(i,-1,-1):
                    if Lall[k][j]==1:
                        size=size+1
                        #t=(k,j)
                        #Lpoint.append(t)
                    else:
                        break
            if Lall[i][j]==0 or j==9:
                #Lallp[size]=Lpoint
                Lsize.append(size)
                size=0
                #Lpoint=[]
                
    largest=max(Lsize)
    #print(largest)
    #print(Lallp[largest])
    return(largest)
                    

def construction_size(i, j1, j2):
    pass
    # Replace pass above with your code

            
try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest block construction has {} blocks.'.format(size_of_largest_construction()))
#size_of_largest_construction()
