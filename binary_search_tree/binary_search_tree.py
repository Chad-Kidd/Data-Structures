import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into tree
    def insert(self, value):
        node = BinarySearchTree(value)
    # if value is less than self.value
        if value < self.value:
            # if left is none
            if self.left == None:
                #set left to be node
                self.left = node
      ## if not set left node this value
            else:
                self.left.insert(value)

        else:
      # do same for right side
            if value >= self.value:
        
                if self.right == None:
         
                    self.right = node
        ## if it has a node, call self.right.insert with this value
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:

            if self.left:

                return self.left.contains(target)
            else:
                return False
        else:
            # do the same for right
            if target > self.value:
                if self.right:
                    return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


