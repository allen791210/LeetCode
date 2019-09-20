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
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        if root is None:
            return []

        count = 0
        results = []
        nums, closest_val = self.inorder_traversal(root, target)
        start = nums.index(closest_val)
        end = start + 1

        while count < k:
            if start >= 0 and end < len(nums):
                if abs(nums[start] - target) < abs(nums[end] - target):
                    results.insert(0, nums[start])
                    start -= 1
                else:
                    results.append(nums[end])
                    end += 1
            elif start < 0: # Aware: special conditions
                results.append(nums[end])
                end += 1
            else:
                results.insert(0, nums[start])
                start -= 1
            count += 1
        
        return results


    def inorder_traversal(self, root, target):
        if root is None:
            return None

        stack, nums = [], []
        closest_val = float('inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            nums.append(node.val)
            if abs(node.val - target) < abs(closest_val - target):
                closest_val = node.val
            root = node.right
        
        return nums, closest_val