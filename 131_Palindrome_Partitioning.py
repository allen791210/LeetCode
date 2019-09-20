"""
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        
        results = []
        self.dfs(s, 0, [], results)
        return results

    def dfs(self, s, start_idx, combinations, results): # start_idx / combination / results
        if start_idx == len(s):
            results.append(list(combinations)) # deep copy
            return

        for i in range(start_idx, len(s)):
            if self.is_palidrome(s[start_idx : i + 1]): # NOTICE: from [start_idx : i + 1]
                combinations.append(s[start_idx : i + 1])
                self.dfs(s, i + 1, combinations, results)
                combinations.pop()

    def is_palidrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left, right = left + 1, right - 1
        
        return True