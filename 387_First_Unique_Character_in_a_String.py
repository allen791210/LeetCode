"""
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = {}
        for ch in s:
            count_dict[ch] = count_dict.get(ch, 0) + 1
        
        for idx, ch in enumerate(s):
            if count_dict[ch] == 1:
                return idx
        return -1
