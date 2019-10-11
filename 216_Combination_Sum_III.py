"""
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []
        
        combinations = []
        results = []
        self.dfs(k, n, 1, combinations, results)

        return results

    def dfs(self, k, n, start_idx, combinations, results):
        if len(combinations) == k and n == 0:
            results.append(list(combinations))
        
        if len(combinations) == k:
            return

        for i in range(1, 10): # 1 ~ 9
            combinations.append(i)
            self.dfs(k, n - i, i + 1, combinations, results) # i + 1
            combinations.pop()
