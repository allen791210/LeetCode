"""
Input: 
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""

import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        if len(arrays) == 0:
            return []

        heap =[]
        results = []

        for i in range(len(arrays)):
            if len(arrays[i]) == 0:
                continue
            heapq.heappush(heap, (arrays[i][0], i, 0)) # (val, array_num, index)
        
        while heap:
            val, array_num, index = heapq.heappop(heap)
            results.append(val)
            if (index + 1) < len(arrays[array_num]):
                heapq.heappush(heap, (arrays[array_num][index + 1], array_num, index + 1))

        return results