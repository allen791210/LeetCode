"""
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
"""
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        
        max_less_than_k = 0
        A.sort()
        start, end = 0, len(A) - 1

        while start < end:
            if A[start] + A[end] < K:
                start += 1
            elif A[start] + A[end] > K:
                end -= 1
            else:
                return K
            
            if A[start] + A[end] < K and A[start] + A[end] > max_less_than_k:
                max_less_than_k = A[start] + A[end]

        return max_less_than_k