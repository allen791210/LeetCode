"""
Input: ["flower","flow","flight"]
Output: "fl"
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return "" if len(strs) == 0 else strs[0]

        longest_prefix = ""
        min_str =  min(strs, key=len)

        for i, ch in enumerate(min_str):
            for j in range(0, len(strs)):
                if ch != strs[j][i]:
                    return longest_prefix # 直接return, NOT break
                if ch == strs[j][i] and j == len(strs) - 1:
                    longest_prefix += ch

        return longest_prefix