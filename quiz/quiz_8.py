# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by Minkai Li and Eric Martin for COMP9021


import sys
from random import seed, randint

from array_queue import *


dim = 10
grid = [[0] * dim for i in range(dim)]

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def leftmost_longest_path_from_top_left_corner():
    path = []
    queue = ArrayQueue(10000)
    if grid[0][0]:
        queue.enqueue([(0,0)])       
        path = queue.dequeue()     
        if grid[1][0]:          
            queue.enqueue([(0,0),(1,0)])
        if grid[0][1]:
            queue.enqueue([(0,0),(0,1)])
    while not queue.is_empty():
        path=queue.dequeue()
        if path[-1][0]==path[-2][0]+1:#down
            if path[-1][1]-1>=0 and (path[-1][0],path[-1][1]-1) not in path \
               and grid[path[-1][0]][path[-1][1]-1]==1:#go right
                queue.enqueue(path + [(path[-1][0],path[-1][1]-1)])
            if path[-1][0]+1<dim and (path[-1][0]+1,path[-1][1]) not in path \
               and grid[path[-1][0]+1][path[-1][1]]==1:#go striaght
                queue.enqueue(path + [(path[-1][0]+1,path[-1][1])])
            if path[-1][1]+1<dim and (path[-1][0],path[-1][1]+1) not in path \
               and grid[path[-1][0]][path[-1][1]+1]==1:#go left
                queue.enqueue(path + [(path[-1][0],path[-1][1]+1)])
        if path[-1][1]==path[-2][1]+1:#right
            if path[-1][0]+1<dim and (path[-1][0]+1,path[-1][1]) not in path \
               and grid[path[-1][0]+1][path[-1][1]]==1:#go right
                queue.enqueue(path + [(path[-1][0]+1,path[-1][1])])
            if path[-1][1]+1<dim and (path[-1][0],path[-1][1]+1) not in path \
               and grid[path[-1][0]][path[-1][1]+1]==1:#go striaght
                queue.enqueue(path + [(path[-1][0],path[-1][1]+1)])
            if path[-1][0]-1>=0 and (path[-1][0]-1,path[-1][1]) not in path \
               and grid[path[-1][0]-1][path[-1][1]]==1:#go left
                queue.enqueue(path + [(path[-1][0]-1,path[-1][1])])
        if path[-1][0] == path[-2][0] - 1:#up
            if path[-1][1]+1<dim and (path[-1][0],path[-1][1] + 1) not in path \
               and grid[path[-1][0]][path[-1][1] + 1] == 1:#go right
                queue.enqueue(path + [(path[-1][0],path[-1][1] + 1)])
            if path[-1][0]-1>=0 and (path[-1][0] - 1,path[-1][1]) not in path \
               and grid[path[-1][0] - 1][path[-1][1]] == 1:#go striaght
                queue.enqueue(path + [(path[-1][0] - 1,path[-1][1])])
            if path[-1][1] - 1>=0 and (path[-1][0],path[-1][1] - 1) not in path \
               and grid[path[-1][0]][path[-1][1] - 1] == 1:#go left
                queue.enqueue(path + [(path[-1][0],path[-1][1] - 1)])
        if path[-1][1] == path[-2][1] - 1:#left
            if path[-1][0] - 1>=0 and (path[-1][0] - 1,path[-1][1]) not in path \
               and grid[path[-1][0] - 1][path[-1][1]] == 1:#go right
                queue.enqueue(path + [(path[-1][0] - 1,path[-1][1])])
            if path[-1][1] - 1>=0 and (path[-1][0],path[-1][1] - 1) not in path \
               and grid[path[-1][0]][path[-1][1] - 1] == 1:#go striaght
                queue.enqueue(path + [(path[-1][0],path[-1][1] - 1)])
            if path[-1][0] + 1<dim and (path[-1][0] + 1,path[-1][1]) not in path \
               and grid[path[-1][0] + 1][path[-1][1]] == 1:#go left
                queue.enqueue(path + [(path[-1][0] + 1,path[-1][1])])
    return path
    pass
    # Replace pass above with your code

provided_input = input('Enter one integer: ')
try:
    seed_arg = int(provided_input)
except:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/2 to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = randint(0, 1)
print('Here is the grid that has been generated:')
display_grid()

path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner')
else:
    print('The leftmost longest path from the top left corner is {}'.format(path))
           
