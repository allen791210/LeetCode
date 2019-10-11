"""
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        return self.dfs_min_path(triangle, 0, 0)

    def dfs_min_path(self, triangle, x, y):
        if x == len(triangle):
            return triangle[x][y]

        left = self.dfs_min_path(triangle, x + 1, y)
        right = self.dfs_min_path(triangle, x + 1, y + 1)

        return min(left + triangle[x][y], right + triangle[x][y])