class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    """
    [6,8,9,1,2] -> [1,2,6,8,9]
    """
    def recoverRotatedSortedArray(self, nums):
        start_idx = 0
        for i in range(len(nums)):
            if nums[i] > nums[i + 1]:
                start_idx = i + 1
                break
        
        nums = nums[start_idx:] + nums[:start_idx]
        return nums


a = Solution()
nums = [4,5,1,2,3]
print(a.recoverRotatedSortedArray(nums))



