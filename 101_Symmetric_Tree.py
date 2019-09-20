"""
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections.deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isChildrenSymmetric(root.left, root.right)

    def isChildrenSymmetric(self, left, right):
        if left == right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val == right.val:
            return self.isChildrenSymmetric(left.left, right.right) and self.isChildrenSymmetric(left.right, right.left)
        else:
            return False
        





            