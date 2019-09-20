class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    # O(N)
    def winSum(self, nums, k):
        if nums == 0 or k == 0 or k > len(nums):
            return []

        sums = [0] *(len(nums) - k + 1) # KEY: - (k - 1)
        for i in range(k):
            sums[0] += nums[i]
        
        for i in range(1, len(nums) - k + 1):
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i + k - 1] # KEY: 下一個sum = 減頭加尾     

        return sums

    
    # O(KN)
    def winSum(self, nums, k):
        if nums == 0 or k == 0 or k > len(nums)::
            return []

        results = []
        for i in range(len(nums) - k + 1): # - (k - 1)
            tmp_sum = 0
            for j in range(k):
                tmp_sum += nums[i + j]
            results.append(tmp_sum)

        return results

"""
Input：array = [1,2,7,8,5], k = 3
Output：[10,17,20]
"""