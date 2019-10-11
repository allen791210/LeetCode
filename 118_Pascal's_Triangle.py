"""
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
             return []
        
        pascal = []
        for i in range(1, numRows + 1):
            pascal.append([0] * i)

        pascal[0][0] = 1
        for i in range(1, numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    pascal[i][j] = 1
                else:
                    pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal
"""
                else:
                    if pascal[i][j]:
                        continue
                    else:
                        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
                        pascal[i][-j - 1] = pascal[i][j]
"""
        