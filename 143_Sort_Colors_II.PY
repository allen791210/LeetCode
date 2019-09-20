class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, nums, k):
        if nums == []:
            return None
        
        start_idx = 0
        for i in range(1, k + 1):
            start_idx = self.partition(nums, start_idx, len(nums) - 1, i)
        
    def partition(self, nums, start, end, val):
        left, right = start, end
        
        while left <= right:
            while left <= right and nums[left] <= val:
                left += 1
            while left <= right and nums[right] > val:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        
        return left