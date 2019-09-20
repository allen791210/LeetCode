"""
Input: arr = [1,-2,1], k = 5
Output: 2

1 -2 3 1 -2 3
"""

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        
        new_arr = arr * k
        for i in range(1, len(new_arr)):
            new_arr[i] = max(new_arr[i], new_arr[i] + new_arr[i -1])

        if max(new_arr) > 0:
            return max(new_arr)
        else:
            return 0