'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''
from typing import List
class Solution:
    def findKth(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # consider empty case, corner case
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        half1, half2 = len(nums1)//2, len(nums2)//2 
        m1, m2 = nums1[half1], nums2[half2]

        if k > half1 + half2:
            if m1 > m2:
                return self.findKth(nums1, nums2[half2 + 1:], k - half2 - 1)
            else:
                return self.findKth(nums1[half1 + 1:], nums2, k - half1 - 1)
        else:
            if m1 > m2:
                return self.findKth(nums1[:half1], nums2, k)
            else:
                return self.findKth(nums1, nums2[:half2], k)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:            
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return self.findKth(nums1, nums2, total_len // 2) #index based
        else:
            return (self.findKth(nums1, nums2, total_len // 2) + self.findKth(nums1, nums2, total_len // 2 - 1)) / 2
        

s = Solution()
nums1 = []
nums2 = [2, 3]
print(s.findMedianSortedArrays(nums1, nums2))