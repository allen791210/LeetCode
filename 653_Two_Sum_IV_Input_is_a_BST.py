# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
"""

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        
        num_set = set()
        return self.inorder_traversal(root, set(), k)

    def inorder_traversal(self, root, num_set, k):
        if not root:
            return False

        l = self.inorder_traversal(root.left, num_set, k)
        if k - root.val in num_set:
            return True
        else:
            num_set.add(root.val)
        r = self.inorder_traversal(root.right, num_set, k)
        
        return l or r