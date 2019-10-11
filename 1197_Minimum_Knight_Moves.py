"""
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
"""
import collections
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0

        return self.bfs_path(0, 0, x, y)

    def bfs_path(self, start_x, start_y, target_x, target_y):
        count = 0
        visited = set()
        queue = collections.deque([(start_x, start_y)])
        directions = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
        while queue:
            for i in range(len(queue)):
                head = queue.popleft()
                cur_x, cur_y = head[0], head[1]
                if cur_x == target_x and cur_y == target_y:
                    return count
                
                cur_dist = self.cal_dist(cur_x, cur_y, target_x, target_y)
                for i, j in directions:
                    if (cur_x + i, cur_y + j) not in visited and self.cal_dist(cur_x + i, cur_y + j, target_x, target_y) < cur_dist: # 先判斷再計算
                        queue.append((cur_x + i, cur_y + j))
                        visited.add((cur_x + i, cur_y + j))

            count += 1
        
        return count - 1
        
    def cal_dist(self, x, y, target_x, target_y):
        return (target_x - x) * (target_x - x) + (target_y - y) * (target_y - y) # **2 slowly
