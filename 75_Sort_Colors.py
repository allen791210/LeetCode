class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Input : [1, 0, 1, 2]
        Output : [0, 1, 1, 2]
        Explanation : sort it in-place
        """
        if nums == []:
            return None
        
        new_start_idx = self.partition(nums, 0, len(nums) - 1, 0)
        self.partition(nums, new_start_idx, len(nums) - 1, 1)
    
    def partition(self, nums, start, end, val):
        left, right = start, end
        
        while left <= right:
            while left <= right and nums[left] == val:
                left += 1
            while left <= right and nums[right] > val:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        
        return left

    # 九章解答 
    """
    使用一次掃瞄的辦法。
    設立三根指針，left, index, right。定義如下規則：

    left 的左側都是 0（不含 left）
    right 的右側都是 2（不含 right）
    index 從左到右掃瞄每個數，如果碰到 0 就丟給 left，碰到 2 就丟給 right。碰到 1 就跳過不管
    """
    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1

        # be careful, index < right is not correct
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1
            elif A[index] == 1:
                index += 1
            else:
                A[right], A[index] = A[index], A[right]
                right -= 1 # 因為right交換過來的數字大小不明，必須再次檢查，因此index"不能" +1
        
        