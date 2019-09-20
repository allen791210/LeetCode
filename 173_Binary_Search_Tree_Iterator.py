# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [] # KEY: iterator -> use stack
        while root is not None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:        
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        val = node.val
        if node.right: # KEY: consider if the smallest node's right node exists?
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        
        return val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0



"""
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()