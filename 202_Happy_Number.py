"""
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        
        num_set = set()
        while n not in num_set:
            num_set.add(n)
            tmp = 0
            while n != 0:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp
            if n == 1:
                return True

        return False