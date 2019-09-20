"""
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

TIME: O(N+M)
SPACE: O(N+M)
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        res = []

        for n in nums2:
            if counts[n] > 0:
                counts[n] -= 1
                res.append(n)

        return res