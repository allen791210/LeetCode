"""
Input:nums = [1,1,1], k = 2
Output: 2

Time:
Space:
KEY: use prefix sum
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        prefix_sum_dict = {0: 1} # {sum: freq.} # KEY: Initilization: {0: 1} empty array = 0

        for idx, n in enumerate(nums):
            prefix_sum += n
            if prefix_sum - k in prefix_sum_dict:
                result += prefix_sum_dict[prefix_sum - k]
            
            if prefix_sum in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] += 1
            else:
                 prefix_sum_dict[prefix_sum] = 1

        return result
