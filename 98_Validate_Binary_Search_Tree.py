# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Set limit range:
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, -sys.maxsize, sys.maxsize)

    def validate(self, root, min_val, max_val):
        if root is None:
            return True
        if root.val <= min_val or root.val >= max_val: # out of range, aware: "="
            return False
        # root.left must < root.val, root.right must > root.val
        return self.validate(root.left, min_val, root.val) and self.validate(root.right, root.val, max_val)

#inorder traversal
class Solution():
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = []
        pre_node = None
        while root or stack: # It's "or" here
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop() # Must use "ROOT" to catch pop node
            if pre_node and pre_node.val >= root.val:
                return False
            pre_node = root
            root = root.right

        return True

# divide & conquer
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)

        if left and right:
            if root.left and root.val <= root.left.val: # onlu locally, need globally
                return False
            if root.right and root.val >= root.right.val:
                return False
            return True
        else:
            return False
# {10,5,#,1,100}

# [10,5,15,null,null,6,20]