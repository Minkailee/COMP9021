# Code for insertion into a priority queue
# implemented as a binary tree
#
# Written by minkaili for COMP9021


from binary_tree import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.left_node =BinaryTree()
            self.right_node =BinaryTree()
            return True
        newnode=self.size()+1
        level=int(log(self.size,2))
        nub_in_level=2**level
        first_nb_in_level=nub_in_level
        node=self
        rootnode=[node]
        for i in range(level-1):
            nub_in_level//=2
            if newnode<first_nb_in_level+nub_in_level:
                node=node.leftnode
            else:
                first_nb_in_level+=nub_in_level
                node=node.rightnode
            rootnode.append(node)
        if first_nb_in_level==newnode:
            node.leftnode=BinaryTree(value)
            parentnode.append(node.leftnode)
        else:
            node.rightnode=BinaryTree(value)
            parentnode.append(node.rightnode)
        while rootnode:
            childnode=parentnode
            parentnode=rootnode.pop()
            if childnode.value<parentnode.value:
                childnode.value,parentnode.value=parentnode.value,childnode.value
                # Replace pass above with your code
