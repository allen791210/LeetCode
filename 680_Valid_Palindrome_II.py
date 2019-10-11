"""
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                remove_left_ch = s[left + 1: right + 1]
                remove_right_ch = s[left: right]
                return remove_left_ch == remove_left_ch[::-1] or remove_right_ch == remove_right_ch[::-1]
                
        return True