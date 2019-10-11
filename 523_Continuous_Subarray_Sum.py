"""
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        prefix_sum_dict = {0 : 1} # sum: freq
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum % k == 0:
                return True
            for key in prefix_sum_dict:
                if (prefix_sum - key) % k == 0:
                    return True
            
            if prefix_sum in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] += 1
            else:
                prefix_sum_dict[prefix_sum] = 1

        return False
            