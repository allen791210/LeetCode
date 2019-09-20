"""
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

TIME: O(N + M)
SPACE: O(1)
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))