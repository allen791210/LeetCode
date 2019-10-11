"""
Input: 3
Output: [1,3,3,1]
sol:
  1 2 1 0
+ 0 1 2 1
-----------
  1 3 3 1
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        pascal = [0] * (rowIndex + 1)
        pascal[0] = 1

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1): # not include 0
                pascal[j] += pascal[j - 1] # new value = current value + previous_index value
        
        return pascal