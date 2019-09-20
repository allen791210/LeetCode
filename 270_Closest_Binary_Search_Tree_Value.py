"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    Input: root = {5,4,9,2,#,8,10} and target = 6.124780
    Output: 5
    """
    def closestValue(self, root, target):
        if root is None:
            return None

        upper_node = root 
        lower_node = root
        while root is not None: # Key: find upper and lower bound
            if target > root.val:
                lower_node = root
                root = root.right
            elif target < root.val:
                upper_node = root
                root = root.left
            else:
                return root.val

        if abs(upper_node.val - target) < abs(lower_node.val - target):
            return upper_node.val
        else:
            return lower_node.val
        
        
        