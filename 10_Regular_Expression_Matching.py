"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
Input:
s = "aab"
p = "c*a*b"

s = aaab
p = a*b
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
"""

# DP methodm Time: O(MN), Space: O(MN)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # table[i][j] means the match status between s[:i] and p[:j], so ues len + 1
        match_table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)] # [col for _ row number]
        match_table[0][0] = True
        
        # Update the corner case: s is an empty string but p is not.
        # p need to be a*b*c*..... pattern
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*': #注意: s,p 和 match_table index 會相差1
                match_table[0][i] = match_table[0][i - 2]
            
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    match_table[i][j] = match_table[i - 1][j - 1]

                if p[j - 1] == '*':
                    match_table[i][j] = match_table[i][j - 2] # * = 0
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.': # 如過*前面的字元和 source字元相同 -> source字元可忽略
                        match_table[i][j] = match_table[i][j - 2] or match_table[i - 1][j]
            
        return match_table[len(s)][len(p)]

# DFS + DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs_is_match(s, 0, p, 0, {})

    def dfs_is_match(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # source is empty
        if i == len(s):
            self.is_p_empty(p[j:])
            
        if j == len(p):
            return False
        
        # KEY STEP, 因為 * 跟前面的元素有關，所以需要提前判斷
        if j + 1 < len(p) and p[j + 1] == '*':
            matched = self.char_match(s[i], p[j]) and self.dfs_is_match(s, i + 1, p, j, memo) or \
                self.dfs_is_match(s, i, p, j + 2, memo) # e.g. 略過 "c*"
        else: 
            matched = self.char_match(s[i], p[j]) and \
                self.dfs_is_match(s, i + 1, p, j + 1, memo)
        
        memo[(i, j)] = matched
        return matched

    def char_match(self, s, p):
        return s == p or p == '.'

    # KEY Step
    # source is empty -> p need to be "x*x*..." format to be empty too    
    def is_p_empty(self, p):
        if len(p) % 2 == 1:
            return False
        
        # Pattern: odd idx should all be *
        for idx in range(1, len(p), 2):
            if p[idx] != '*':
                return False
        
        return True
