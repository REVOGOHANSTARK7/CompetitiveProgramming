class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)
        """
        Return True if the find_val is in the tree and False otherwise.
        """
        
    def print_tree(self):
        return self.preorder_print(self.root, "")
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
    
    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False
        
        """
        Helper method - use this to create a 
        recursive search solution.
        """

    def preorder_print(self, start, traversal):
        """Root->Left-Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
        """
        Helper method - use this to create a recursive print solution.
        """
       
