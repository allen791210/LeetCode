"""
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left: leftmost index of zero
        # right: explore the number, if the number != 0, we want to switch it with left
        left, right = 0, 0
        while right < len(nums): 
            if nums[right] != 0: # KEY: != 0, switch and left moves
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1 # Right always moves