class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == None and root2 == None:
            return True
        
        leaves1, leaves2 = [], []
        self.dfs_leaves(root1, leaves1)
        self.dfs_leaves(root2, leaves2)
        
        return leaves1 == leaves2

    def dfs_leaves(self, root, leaves):
        if not root:
            return
        
        if root.left == None and root.right == None:
            leaves.append(root.val)
        
        self.dfs_leaves(root.left, leaves)
        self.dfs_leaves(root.right, leaves)



