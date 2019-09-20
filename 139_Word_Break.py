"""
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False

        def dfs(s, memo, wordDict):
            if s in memo:
                return memo[s]

            if s in wordDict:
                memo[s] = True
                return True
            
            # 1st way
            for i in range(1, len(s)):
                prefix = s[:i]
                if prefix in wordDict and dfs(s[i:], memo, wordDict):  # right in dict, check left string
                    memo[s] = True
                    return True
            
            # 2nd way
            for word in wordDict:
                if s.startswith(word) and dfs(s[len(word):], memo, wordDict):
                    memo[s] = True
                    return True

            memo[s] = False
            return False

        return dfs(s, {}, set(wordDict))