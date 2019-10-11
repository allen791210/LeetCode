"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        self.minumum_weight = sys.maxsize   # use instance variable
        self.subtree = None
        self.helper(root)

        return self.subtree

    def helper(self, root):    
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        root_weight = left + right + root.val

        if root_weight < self.minumum_weight: 
            self.subtree = root
            self.minumum_weight = root_weight

        return root_weight # return total weight, min_weight is recorded by self.minumum_weight 


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        minimum, subtree, sum_ = self.helper(root)
        return subtree
    
    def helper(self, root):
        