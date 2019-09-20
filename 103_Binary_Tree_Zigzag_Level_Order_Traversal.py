"""
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque([root])
        z_traversal = []
        num_level = 0
        while queue:
            level = collections.deque([])
            for i in range(len(queue)):
                head = queue.popleft()
                # KEY: different order to put in list
                if num_level % 2 == 0:
                    level.append(head.val)
                else:
                    level.appendleft(head.val)
                
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            z_traversal.append(level)
            num_level += 1

        return z_traversal