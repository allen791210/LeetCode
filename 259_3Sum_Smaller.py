"""
Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
"""

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        total_smaller_sets = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < target:
                    total_smaller_sets += (right - left)
                    left += 1
                else:
                    right -= 1
        
        return total_smaller_sets
