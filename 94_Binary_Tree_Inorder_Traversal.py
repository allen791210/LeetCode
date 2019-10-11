# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursively, traverse
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        results = []
        self.traverse(root, results)
        return results
    
    def traverse(self, root, results):
        if root is None:
            return
        self.traverse(root.left, results)
        results.append(root.val)
        self.traverse(root.right, results)

# iteratively
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # left -> root -> right
        results, stack = [], []
        cur = root
        while cur or stack: # KEY: current node not none "or" stack is not empty
            while cur is not None:
                stack.append(cur)
                cur = cur.left # check to the leftmost leave
            cur = stack.pop()
            results.append(cur.val)
            cur = cur.right # check if any right leave

        return results