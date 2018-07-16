# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


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
    matrix = []
    for i in range(10):
        for j in range(10):
            matrix.append((i,j))
    result = []
    root = (0,0)
    queue = ArrayQueue(100)
    if grid[root[0]][root[1]]:
        queue.enqueue([root])       
        result = queue.dequeue()     
        if grid[1][0]:            
            queue.enqueue([root] + [(1,0)])
        if grid[0][1]:
            queue.enqueue([root] + [(0,1)])
    print(queue._data)
    while not queue.is_empty():
        result = queue.dequeue()
        if result[-1][0] == result[-2][0] + 1:
            if (result[-1][0],result[-1][1] - 1) in matrix and (result[-1][0],result[-1][1] - 1) not in result:
                if grid[result[-1][0]][result[-1][1] - 1] == 1:
                    queue.enqueue(result + [(result[-1][0],result[-1][1] - 1)])
            if (result[-1][0] + 1,result[-1][1]) in matrix and (result[-1][0] + 1,result[-1][1]) not in result:
                if grid[result[-1][0] + 1][result[-1][1]] == 1:
                    queue.enqueue(result + [(result[-1][0] + 1,result[-1][1])]) 
            if (result[-1][0],result[-1][1] + 1) in matrix and (result[-1][0],result[-1][1] + 1) not in result:
                if grid[result[-1][0]][result[-1][1] + 1] == 1:
                    queue.enqueue(result + [(result[-1][0],result[-1][1] + 1)])
        if result[-1][1] == result[-2][1] + 1:
            if (result[-1][0] + 1,result[-1][1]) in matrix and (result[-1][0] + 1,result[-1][1]) not in result:
                if grid[result[-1][0] + 1][result[-1][1]] == 1:
                    queue.enqueue(result + [(result[-1][0] + 1,result[-1][1])])
            if (result[-1][0],result[-1][1] + 1) in matrix and (result[-1][0],result[-1][1] + 1) not in result:
                if grid[result[-1][0]][result[-1][1] + 1] == 1:
                    queue.enqueue(result + [(result[-1][0],result[-1][1] + 1)])        
            if (result[-1][0] - 1,result[-1][1]) in matrix and (result[-1][0] - 1,result[-1][1]) not in result:
                if grid[result[-1][0] - 1][result[-1][1]] == 1:
                    queue.enqueue(result + [(result[-1][0] - 1,result[-1][1])])

        if result[-1][0] == result[-2][0] - 1:
            if (result[-1][0],result[-1][1] + 1) in matrix and (result[-1][0],result[-1][1] + 1) not in result:
                if grid[result[-1][0]][result[-1][1] + 1] == 1:
                    queue.enqueue(result + [(result[-1][0],result[-1][1] + 1)])
            if (result[-1][0] - 1,result[-1][1]) in matrix and (result[-1][0] - 1,result[-1][1]) not in result:
                if grid[result[-1][0] - 1][result[-1][1]] == 1:
                    queue.enqueue(result + [(result[-1][0] - 1,result[-1][1])])
            if (result[-1][0],result[-1][1] - 1) in matrix and (result[-1][0],result[-1][1] - 1) not in result:
                if grid[result[-1][0]][result[-1][1] - 1] == 1:
                    queue.enqueue(result + [(result[-1][0],result[-1][1] - 1)])
        if result[-1][1] == result[-2][1] - 1:
            if (result[-1][0] - 1,result[-1][1]) in matrix and (result[-1][0] - 1,result[-1][1]) not in result:
                if grid[result[-1][0] - 1][result[-1][1]] == 1:
                    queue.enqueue(result + [(result[-1][0] - 1,result[-1][1])])
            if (result[-1][0],result[-1][1] - 1) in matrix and (result[-1][0],result[-1][1] - 1) not in result:
                if grid[result[-1][0]][result[-1][1] - 1] == 1:
                    queue.enqueue(result + [(result[-1][0],result[-1][1] - 1)])
            if (result[-1][0] + 1,result[-1][1]) in matrix and (result[-1][0] + 1,result[-1][1]) not in result:
                if grid[result[-1][0] + 1][result[-1][1]] == 1:
                    queue.enqueue(result + [(result[-1][0] + 1,result[-1][1])])
    ##print(queue._data)
    return result
    
        


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
           
