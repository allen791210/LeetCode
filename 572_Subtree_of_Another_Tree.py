# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
     3
    / \
   4   5
  / \
 1   2

   4 
  / \
 1   2
"""
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return t is None
        
        if s.val == t.val and self.compare(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def compare(self, s, t):
        if s is None:
            return t is None
        
        if t is None or s.val != t.val:
            return False
        
        return self.compare(s.left, t.left) and self.compare(s.right, t.right)

