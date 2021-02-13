"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from linked_list import LinkedList, Stack, Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if empty
        if self.value == None:
            # if empty, insert here
            self.value = BSTNode(value)
        # elif value < self.value:
        elif value < self.value:
            # insert self.left
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # else:
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == value return
        if target == self.value:
            return True
        # elif target < value 
        elif target < self.value:
            # if node.left exists
            if self.left:
                # traverse left
                return self.left.contains(target)
            # else return False
            else:
                return False
        # elif target > traverse right
        elif target > self.value:
            # if node.right exists
            if self.right:
                # traverse right
                return self.right.contains(target)
            # else return False
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if node has a right
        if self.right:
            #   traverse that
            return self.right.get_max()
        return self.value

    # Call the function `fn` on the value of each node
    """ what is/where is "fn" coming from? It's not a function, it's a parameter..."""
    def for_each(self, fn):
        # if self.value, call fn
        if self.value:
            fn(self.value)
        # if self.left, recurse on self left
        if self.left:
            self.left.for_each(fn)
        # if self. right, recurse on self right
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def get_min(self):
            # if node has a right
            if self.left:
                #   traverse that
                return self.left.get_min()
            return self.value

    def in_order_print(self, node):
        if node == None:
                return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)       
        
        # queue = Queue()
        # queue.enqueue(node)        
        
        # while queue:
        #     value = queue.dequeue()
        #     node.in_order_print(node.left)
        #     queue.enqueue(node)
        #     if value.left == None:
        #     # check for a deeper left value recursively
        #         print(value.value)
        #     if value.left:
        #         value.left.get_min() 
        #     if:
        #         value.right.get_min() 

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        self.queue = Queue()
        self.queue.enqueue(node)
        while self.queue:
            value = self.queue.dequeue()
            print(value.value)
            if value.left:
                self.queue.enqueue(value.left)
            if value.right:
                self.queue.enqueue(value.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack = Stack()
        self.stack.push(node)
        while self.stack:
            value = self.stack.pop()
            print(value.value)
            if value.left:
                self.stack.push(value.left)
            if value.right:
                self.stack.push(value.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
