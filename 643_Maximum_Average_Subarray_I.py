"""
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Key: Sum of Sliding window
Time: O(N)
Space: O(1)
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_max = 0
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        current_max = current_sum
        
        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i - k]
            current_max = max(current_sum, current_max)

        return current_max/k