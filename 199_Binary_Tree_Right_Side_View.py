# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""
import collections
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        results = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                head = queue.popleft()
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
        
                if i == level_length - 1:
                    results.append(head.val)
        
        return results