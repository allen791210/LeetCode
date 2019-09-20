"""
Input: sticks = [2,4,3]
Output: 14
"""
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:     
        total_cost = 0
        heapq.heapify(sticks)
        
        while len(sticks) > 1:
            tmp = heapq.heappop(sticks)
            tmp += heapq.heappop(sticks)
            heapq.heappush(sticks, tmp)
            total_cost += tmp
        
        return total_cost