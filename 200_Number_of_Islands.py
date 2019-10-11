from collections import deque
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        visited = set() # use "set" to record visited nodes, avoid duplicates, set.add()
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.bfs(grid, i, j, visited) # find all adjacent 1's
                    num_islands += 1

        return num_islands

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)]) # KEY: [(x, y)] List of sets
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # use list of delta_x and delta_y
                next_x = x + delta_x
                next_y = y + delta_y
                if self.is_valid(grid, next_x, next_y, visited):
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y)) # add visited nodes here to avoid duplicate proceessing on the same nodes

    def is_valid(self, grid, x, y, visited):
        num_row = len(grid)
        num_coloum = len(grid[0])

        return 0 <= x < num_row and 0 <= y < num_coloum and grid[x][y] == 1 and (x, y) not in visited # in the range, (x, y) == 1 and not visited


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.dfs_mark_island(grid, i, j, visited)
                    count += 1

        return count

    def dfs_mark_island(self, grid, i, j, visited):
        if not self.is_lsland(grid, i, j, visited):
            return
        #grid[i][j] = '#'
        visited.add((i, j))
        for x_step, y_step in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            self.dfs_mark_island(grid, i + x_step, j + y_step, visited)
            
    def is_lsland(self, grid, i, j, visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1' or (i, j) in visited:
            return False
        else:
            return True