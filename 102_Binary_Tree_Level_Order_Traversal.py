# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root]) # Use "deque"
        results = []
        while queue:
            level = []
            # size = len(queue) for C++
            for _ in range(len(queue)): # level order, 注意length是否會改變, python中len(queue)是固定值, C++則否
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)
        
        return results 


