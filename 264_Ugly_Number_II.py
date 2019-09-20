"""
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
"""
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set() # 2*3 == 3*2
        
        for i in range(n):
            value = heapq.heappop(heap) # min_value
            for j in (2, 3, 5):
                if value * j not in visited:
                    visited.add(value * j)
                    heapq.heappush(heap, value * j)

        return value


