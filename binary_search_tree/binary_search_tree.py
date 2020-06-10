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
        print("\n", target, self.value)
        if target == self.value:
            print("TRUE: ", target, self.value)
            """ it's printing out both 7s, so why isn't True returning? """
            return True
        # elif target < value 
        elif target < self.value:
            # if node.left exists
            if self.left:
                print("LEFT: ", self.left)
                # traverse left
                self.value = self.left
                self.value.contains(target)
            # else return False
            else:
                return False
        # elif target > traverse right
        elif target > self.value:
            # if node.right exists
            if self.right:
                print("RIGHT: ", self.right.value)
                # traverse right
                self.value = self.right
                self.value.contains(target)
            # else return False
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        print("\nVal: ", self.value)
        # if node has a right
        max = self.value
        if self.right:
            print("Right: ", self.right.value)
            #   traverse that
            # self.value = self.right
            max = self.right.value
            self.right.get_max()
        # else return node
        # else:
        #     print("MAX", self.value)
        #     """ it's printing out 30, so why isn't 30 getting returned? """
        #     return 
        return max
            # return int(self.value)
            # return BSTNode(self.value)
            # return BSTNode(self.value).value


    # Call the function `fn` on the value of each node
    """ what is/where is "fn" coming from? It's not a function, it's a parameter..."""
    def for_each(self, fn):
        # if self.value, call fn
        print(self.value)
        if self.value:
            print("A")
            return self.value
        # if self.left, recurse on self left
        if self.left:
            print("B")
            self.value = self.left
            self.value.fn()
        # if self. right, recurse on self right
        if self.right:
            print("C")
            self.value = self.right
            self.value.fn()

    # Part 2 -----------------------

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

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
