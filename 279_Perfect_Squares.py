"""
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Thoughts: 
1 + numSquares(12 -1)
4 + numSquares(12 - 4)
9 + numSquares(12 -9)...
"""
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp_min_squares = []
        