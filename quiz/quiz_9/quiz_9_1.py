# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from binary_tree import *

def print_tree_growing_down(tree):
    global filled_tree
    filled_tree =[]
    for i in range(tree.height()+1):
        filled_tree.append([])
    fill_tree(tree,0,tree.height())
    filled_tree.reverse()
    #print(filled_tree)
    for i in range(len(filled_tree)):
        final_tree=''
        final_tree += ' '*(2**i - 1 )
        for j in filled_tree[i]:
            final_tree += str(j) + ' ' * (2**(i+1)-1)
        print(final_tree)
def fill_tree(self,level,height):    
    if level > height:
        return
    if self.value is not None:
        fill_tree(self.left_node,level+1,height)
        fill_tree(self.right_node,level+1,height)
        filled_tree[level].append(self.value)     
    else:
        for i in range(level,height+1):
            for _ in range (2**(i-level)):
                filled_tree[i].append(' ')
# Possibly write additional function(s)
        

provided_input = input('Enter two integers, with the second one between 0 and 10: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
print_tree_growing_down(tree)
           
