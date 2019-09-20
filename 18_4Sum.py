"""
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
[-2 -1 0 0 1 2]
"""
from typing import List
class Solution:
    def findNSum(self, nums, l, r, N, target, tmp_result, results):
        # N < 2 terminate, other early termination conditions
        if N < 2 or (r - l + 1) < N or sum(nums[l:l + N]) > target or sum(nums[r + 1 - N:r + 1]) < target:
            return
        if N == 2:
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    while l < r and nums[l + 1] == nums[l]: l += 1
                    l += 1 
                elif s > target:
                    while l < r and nums[r - 1] == nums[r]: r -= 1
                    r -= 1
                else:
                    results.append(tmp_result + [nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]: l += 1
                    while l < r and nums[r - 1] == nums[r]: r -= 1
                    l += 1; r -= 1
        else:
            for i in range(l, r + 1): # Be careful about the range
                if i == l or (i > l and nums[i] != nums[i - 1]):
                    self.findNSum(nums, i + 1, r, N - 1, target - nums[i], tmp_result + [nums[i]], results)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:    
        nums.sort()
        results = []
        self.findNSum(nums, 0, len(nums) - 1, 4, target, [], results)
        return results

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        results = []
        numbers.sort()
        for i in range(len(numbers) - 3):
            if numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, len(numbers) - 2):
                if j != i + 1 and numbers[j] == numbers[j - 1]: # Notice: j != i + 1, 如果剛好 j = i+1 and numbers[i] == numbers[j], 必須考慮此case，非重複
                    continue
                left, right = j + 1, len(numbers) - 1
                while left < right:
                    s = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else: # == target
                        results.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left += 1; right -= 1
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1
                        
        return results
"""        
CASE:
[1,0,-1,-1,-1,-1,0,1,1,1,2]
2
Output
[[-1,0,1,2],[-1,1,1,1]]
Expected
[[-1,0,1,2],[-1,1,1,1],[0,0,1,1]]
"""


s = Solution()
# nums = [1, 0, -1, 0, -2, 2]
# nums = [-1,-5,-5,-3,2,5,0,4]
nums = [-5,5,4,-3,0,0,4,-2]
# 0 case, [0,0,0,0]
# consider corner case e.g. nums < N, answer not exist 
print(s.fourSum(nums, 0))
