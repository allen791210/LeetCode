"""
Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
"""
DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #visited = set()
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs_island(grid, i, j))
        return max_area
    
    def dfs_island(self, grid, x, y):
        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == 0:
            return 0 # return 0
        
        #visited.add((x, y)) # visited 不管用 多個dfs各自的visited無法sync
        area_sum = 1
        grid[x][y] = 0
        for i, j in DIRECTIONS:
            new_x = x + i 
            new_y = y + j
            area_sum += self.dfs_island(grid, new_x, new_y)

        return area_sum