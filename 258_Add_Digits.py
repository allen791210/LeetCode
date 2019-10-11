"""
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

"""
N=(a[0] * 1 + a[1] * 10 + ...a[n] * 10 ^n),and a[0]...a[n] are all between [0,9]
we set M = a[0] + a[1] + ..a[n] and another truth is that:

1 % 9 = 1
10 % 9 = 1
100 % 9 = 1
so N % 9 = a[0] + a[1] + ..a[n]

means N % 9 = M
so N = M (% 9)
as 9 % 9 = 0,so we can make (n - 1) % 9 + 1 to help us solve the problem when n is 9.as N is 9, ( 9 - 1) % 9 + 1 = 9
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1