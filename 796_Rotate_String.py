"""
Input: A = 'abcde', B = 'cdeab'
Output: true
"""
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A
        