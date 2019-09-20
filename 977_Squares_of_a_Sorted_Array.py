"""
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

import collections

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return []

        A = [-i if i < 0 else i for i in A]        
        results = collections.deque([])
        left, right = 0, len(A) - 1
        
        while left <= right: # key "<="
            if A[left] > A[right]:
                results.appendleft(A[left] ** 2)
                left += 1
            else:
                results.appendleft(A[right] ** 2)
                right -= 1
        
        return results