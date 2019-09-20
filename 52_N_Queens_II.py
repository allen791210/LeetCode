"""
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
             return 0

        results = []
        self.dfs(n, [], [], [], results)
        
        return len(results)

    def dfs(self, n, queens, xy_diif, xy_sum, results):
        if len(queens) == n:
            results.append(queens)
            return

        row = len(queens)
        for col in range(n):
            if col not in queens and (row - col) not in xy_diif and (row + col) not in xy_sum:
                self.dfs(n, queens + [col], xy_diif + [row - col], xy_sum + [row + col], results)
