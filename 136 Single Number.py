class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            result ^=  nums[i]

        #print result
        return result

#test = Solution()
#test.singleNumber([1,3,3,5,5])
