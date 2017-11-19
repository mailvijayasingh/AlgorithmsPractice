# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    first_tree_node = None
    first_tree_node = None
    import sys
    prev=TreeNode(-sys.maxint - 1)
    found_first = False
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if not self.found_first and self.prev.val >= root.val:
            self.first_tree_node = self.prev
            self.found_first = True
        if self.found_first and self.prev.val >= root.val:
            self.second_tree_node = root
        self.prev = root
        self.traverse(root.right)
    
    def recoverTree(self, root):
        self.traverse(root)
        temp = self.first_tree_node.val
        self.first_tree_node.val = self.second_tree_node.val
        self.second_tree_node.val = temp
        
        
        
        
        