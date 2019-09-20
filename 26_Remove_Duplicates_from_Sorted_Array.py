"""
Given nums = [0,0,1,1,1,2,2,3,3,4],
return 5, [0, 1, 2, 3, 4, .......]
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        left = 1 # count for difference
        right = 1
        while right < len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1
        
        return left
            