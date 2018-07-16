# Randomly fills an array of size 10x10 with 0s and 1s, and
# outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by MinkaiLi and Eric Martin for COMP9021


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


def explore_board():
    L=[]
    for i in range(dim+4):
        Line=[]
        if i <=1 or i>=dim+2:
            L.append([0]*14)
        else:
            for j in range(dim+4):
                if j<=1 or j>=dim+2:  
                    Line.append(0)
                else:
                    if grid[i-2][j-2]:
                        Line.append(1)
                    else:Line.append(0)
            L.append(Line)
    n=0
    for x in range(2,12):
        for y in range(2,12):
            if L[x][y]==1:
                n=n+1
                knight(L,x,y)
    return n

def knight(L,x,y):
    L[x][y]=0
    if L[x+1][y+2]==1:
        knight(L,x+1,y+2)
    if L[x+1][y-2]==1:
        knight(L,x+1,y-2)
    if L[x-1][y+2]==1:
        knight(L,x-1,y+2)
    if L[x-1][y-2]==1:
        knight(L,x-1,y-2)
    if L[x+2][y+1]==1:
        knight(L,x+2,y+1)
    if L[x+2][y-1]==1:
        knight(L,x+2,y-1)
    if L[x-2][y+1]==1:
        knight(L,x-2,y+1)
    if L[x-2][y-1]==1:
        knight(L,x-2,y-1)
    return L


try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers: ').split()]
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[None] * dim for _ in range(dim)]
if n > 0:
    for i in range(dim):
        for j in range(dim):
            grid[i][j] = randrange(n) > 0
else:
    for i in range(dim):
        for j in range(dim):
            grid[i][j] = randrange(-n) == 0
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
else:
    print('At least {} chess'.format(nb_of_knights), end = ' ')
    print('knight has', end = ' ') if nb_of_knights == 1 else print('knights have', end = ' ')
    print('explored this board.')

