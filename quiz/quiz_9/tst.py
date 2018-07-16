import sys
from random import seed, choice
from binary_tree import *

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
def fill(height,level,tree):
    if level > height:
       return
    if tree.value is None:
        tree.value=' '
    fill(height,level+1,tree.left_node)
    fill(height,level+1,tree.right_node)
