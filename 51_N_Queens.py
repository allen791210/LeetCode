"""
Input: 4
[[1,3,0,2],[2,0,3,1]]
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return [[]]
        
        results = []
        self.dfs(n, [], [], [], results)
        
        return self.drawResults(results)
    
    def dfs(self, size, queens, xy_diff, xy_sum, results):
        if len(queens) == size:
            results.append(queens)
            return # backtracking ?

        row = len(queens) # no. of queens = row number
        for col in range(size): # col number (0, size)
            # KEY: how to identify if queen is on the same "diagonal" -> x+y & x-y
            if col not in queens and (row - col) not in xy_diff and (row + col) not in xy_sum: # isValid
                self.dfs(size, queens + [col], xy_diff + [row - col], xy_sum + [row + col], results) # queens + [col] -> append & pop

    def drawResults(self, results):
        n = 0
        if len(results) > 0:
            n = len(results[0])
        
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in results]
"""
        tmp = []
        s = []
        for sol in results:
            n = len(sol)
            for i in sol:
                s += ["." * i + "Q" + "." * (n - i - 1)]
            tmp.append(s)
            s = []
        return tmp
"""