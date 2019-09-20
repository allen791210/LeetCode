"""
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        count = 1
        two_dup = True
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1
                two_dup = True
            elif nums[i] == nums[i - 1] and two_dup:
                nums[count] = nums[i]
                count += 1
                two_dup = False

        return count

# LEETCODE
int removeDuplicates(vector<int>& nums, int k) {
    int i = 0;
    for (int n : nums)
        if (i < k || n > nums[i-k]) # KEY
            nums[i] = n;
            i += 1
    return i;
}
        