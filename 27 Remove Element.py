class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums = [i for i in nums if i != val]
        print len(nums)
        return len(nums)
        
test = Solution()
test.removeElement([3,2,2,3], 3)
