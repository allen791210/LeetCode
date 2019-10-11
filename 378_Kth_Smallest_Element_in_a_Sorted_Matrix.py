"""
matrix = [
   [ 1,  5, 12],
   [ 4, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

if self.get_num_smaller_equal(matrix, left) >= k:
CASE: 
[[1,2],[1,3]]
1
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or k == 0:
            return 0

        left = matrix[0][0]
        right = matrix[-1][-1]
        while left + 1 < right:
            mid = (left + right) // 2
            if self.get_num_smaller_equal(matrix, mid) < k: # 不可用 <=
                left = mid
            else:
                right = mid

        if self.get_num_smaller_equal(matrix, left) >= k:
            return left

        return right

    def get_num_smaller_equal(self, matrix, num):
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m - 1
        count = 0
        while i < n and j >= 0:
            if matrix[i][j] <= num:
                i += 1
                count += (j + 1)
            else:
                j -= 1
        
        return count