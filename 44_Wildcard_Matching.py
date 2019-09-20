"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
Input:
s = "adceb"
p = "*a*b"
Output: true
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs_is_match(s, 0, p, 0, {})
    
    # # source 從 i 開始的後綴 能否匹配上 pattern 從 j 開始的後綴
    def dfs_is_match(self, s, i, p, j, memo): # use memo to record
        if (i, j) in memo:
            return memo[(i, j)]
        
        # exit condition: i == len(s), j == len(p)
        if i == len(s): # empty case or i to the end
            for idx in range(j, len(p)): 
                if p[idx] != '*':
                    return False
            return True

        if j == len(p):
            return False

        if p[j] != '*':
            matched = self.is_match_char(s[i], p[j]) and \
                self.dfs_is_match(s, i + 1, p, j + 1, memo)
        else: # KEY STEP
            matched = self.dfs_is_match(s, i + 1, p, j, memo) or \
                self.dfs_is_match(s, i, p, j + 1, memo) # two possible cases: use "or" 
        
        memo[(i, j)] = matched
        return matched

    def is_match_char(self, s, p):
        return s == p or p == '?'

"""
INPUT
"aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab"
"*ab***ba**b*b*aaab*b"
"""