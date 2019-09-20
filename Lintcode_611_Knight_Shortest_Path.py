"""
Definition for a point.
class Point:
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b
"""

from collections import deque
class Solution:        
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        
        distance_map = {(source.x, source.y): 0}
        queue = deque([(source.x, source.y)])
        directions = [ # use a macro way to define directions
            (-2, -1), (-2, 1), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (1, -2), (1, 2)
        ]        
        while queue:
            x, y = queue.popleft()
            if x == destination.x and y == destination.y:
                return distance_map[(x, y)]
            for delta_x, detal_y in directions:
                next_x = x + delta_x
                next_y = y + detal_y
                if (next_x, next_y) in distance_map: # KEY: avoid duplicated calculations / avoid same node into the queue
                    continue
                if self.is_valid(grid, next_x, next_y):
                    queue.append((next_x, next_y))
                    distance_map[(next_x, next_y)] = distance_map[(x, y)] + 1
        
        return -1

    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])

        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 1:
            return False
        else:
            return True

