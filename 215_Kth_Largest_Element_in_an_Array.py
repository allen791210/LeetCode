class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums == [] or k > len(nums):
            return 0

        return self.partition(nums, 0, len(nums) - 1, len(nums) - k) # remember change largest to smallest: k -> len(nums) - k

    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k] # why ?

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right: # Note: need to check again
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1 # Note: need to move left and right

        if k <= right: # end -> right
            self.partition(nums, start, right, k)
        if k >= left: # start -> left
            self.partition(nums, left, end, k)

        return nums[k]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums == [] or k > len(nums):
            return 0
        
        left, right = 0, len(nums) - 1
        k = len(nums) - k
        while (True):
            pos = self.partition(nums, left, right)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 < k:
                left = pos + 1
            else:
                right = pos - 1

    def partition(self, nums, l, r):
        if l == r:
            return nums[l]

        pivot = nums[l]
        left, right = l, r
        
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if nums[left] < nums[right]:
                nums[left], nums[right] = nums[right], nums[left]  

        if nums[left] < nums[right]:
            nums[l], nums[right] = nums[right], nums[l]

        return left
