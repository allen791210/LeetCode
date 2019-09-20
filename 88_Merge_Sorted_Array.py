"""
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n > 0:
            if m == 0 or nums2[n - 1] > nums1[m - 1]: # KEY: m == 0
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
    