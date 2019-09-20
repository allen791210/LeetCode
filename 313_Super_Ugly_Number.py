import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        visited = set() # 2*3 == 3*2
        
        for i in range(n):
            value = heapq.heappop(heap) # min_value
            for j in primes:
                if value * j not in visited:
                    visited.add(value * j)
                    heapq.heappush(heap, value * j)

        return value        