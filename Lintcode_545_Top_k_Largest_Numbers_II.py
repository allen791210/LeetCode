"""
Input: 
s = new Solution(3);
s.add(3)
s.add(10)
s.topk()
s.add(1000)
s.add(-99)
s.topk()
s.add(4)
s.topk()
s.add(100)
s.topk()
		
Output: 
[10, 3]
[1000, 10, 3]
[1000, 10, 4]
[1000, 100, 10]
"""
import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.maxSize = k
        self.Minheap = []
    
    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.Minheap) < self.maxSize:
            heapq.heappush(self.Minheap, num)
        else:
            if num > self.Minheap[0]:
                heapq.heappop(self.Minheap)
                heapq.heappush(self.Minheap, num)

    """
    @return: Top k element
    """
    def topk(self):
        return sorted(self.Minheap, reverse = True)