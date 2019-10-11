# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # KEY: 某個點的左右兩邊同時存在target(p & q) => LCA
        # Found p or q => return
        
        # A & 下面有B => A
        # B & 下面有A => B
        # A & 下面啥都没有 => A
        # B & 下面啥都有 => B 
        if root is None:
            return None
        # 因為如果pq同邊, 先遇到的即為LCA, 直接return，如果不同邊，遇到也是直接return
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # A 和 B 一边一个
        if left and right: 
            return root
        
        # 左子树有一个点或者左子树有LCA
        if left:
            return left
        
        # 右子树有一个点或者右子树有LCA
        if right:
            return right
        
        # 左右子树啥都没有
        return None
               
        
        
        