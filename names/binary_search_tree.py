import sys
#sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If value is less than node's value
        if value < self.value:
            # If None then insert a node on the left
            if not self.left:
                self.left = BinarySearchTree(value)
            # Recursive call until condition `if not self.left`(self.left has None) is satisfied
            else:
                # Goes to the next left node and calls the insert function
                return self.left.insert(value)
        # If value is equal or greater than 
        else:
            # If self.right is nont None then add a node
            if not self.right:
                self.right = BinarySearchTree(value)
            # Recursive call until condition `if not self.right` is satisfied
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case to return true if equal
        if target == self.value:
            return True
        # If the next node is None then return False and stop the recursion
        else:
            if target < self.value:
                if not self.left:
                    return False
                return self.left.contains(target)
            else:
                if not self.right:
                    return False
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        # Run the function on the self.value
        cb(self.value)

        # If true use recursion
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
          node.left.in_order_print(node.left)
        if node.right:
          print(node.value)
          node.right.in_order_print(node.right)
        else:
          print(node.value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        
        while queue.size > 0:
            popped = queue.dequeue()
            print(popped.value)

            if popped:
                if popped.left:
                    queue.enqueue(popped.left)
                if popped.right:
                    queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        '''
        Iterative
        '''
        # Instanstiate Stack
        stack = Stack()

        # Push first node
        stack.push(node)

        # Check if size of stack > 0
        while stack.size > 0:
            # Take the last one
            popped = stack.pop()
            print(popped.value)

            # Check if there's a left or right and pop its value
            if popped:
              if popped.left:
                  stack.push(popped.left)

              if popped.right:
                  stack.push(popped.right)
        '''
        Recursive
        '''
        # print(node.value)
        # if node.right:
        #   node.right.dft_print(node.right)
        # if node.left:
        #   node.left.dft_print(node.left)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
