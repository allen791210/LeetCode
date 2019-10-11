# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        
        tree1_dict = {}
        tree2_dict = {}
        self.inorder_traversal(root1, tree1_dict)
        self.inorder_traversal(root2, tree2_dict)
        #print(tree1_dict, tree2_dict)
        for key in tree1_dict:
            if target - key in tree2_dict:
                return True
            
        return False
    
    def inorder_traversal(self, root, tree_dict):
        if root is None:
            return
        self.inorder_traversal(root.left, tree_dict)
        tree_dict[root.val] = 1
        self.inorder_traversal(root.right, tree_dict)                
        