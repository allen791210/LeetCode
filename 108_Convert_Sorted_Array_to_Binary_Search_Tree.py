# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        
        for i in range(mid):
            dfs(root, nums[i])
        for j in range(mid + 1, len(nums)):
            dfs(root, nums[j])    
        
        return root
    def dfs(self, root, val):
        if val > root.val:
            if root.right:
                self.dfs(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left:
                self.dfs(root.left, val)
            else:
                root.left = TreeNode(val)
