"""
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n or n == 0 or k == 0:
            return []

        results = []
        self.dfs(n, k, 1, [], results)
        
        return results

    def dfs(self, n, k, start_idx, combinations, results):
        if len(combinations) == k:
            results.append(combinations)
            return
        
        for i in range(start_idx, n + 1): # KEY: from start_idx(1) to n+1
            self.dfs(n, k, i + 1, combinations + [i], results)






