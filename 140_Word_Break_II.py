"""
"aaaaaaa"
["aaaa","aa","a"]
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
# 1st solution
        def dfs(s, wordDict, memo):
            if len(s) == 0:
                return []
            if s in memo: # use dp to speed up
                return memo[s]

            results = []
            if s in wordDict:
                results.append(s) # s in wordict 但s 仍有其他組合可能需要繼續判斷

            for i in range(1, len(s)):
                prefix = s[:i] # left
                if prefix in wordDict:
                    partitions = dfs(s[i:], wordDict, memo) # check right part
                    for partition in partitions:
                        results.append(prefix + " " + partition)
            memo[s] = results # 要記住的是整個s 對應的答案
            return results
        return dfs(s, wordDict, {})

        # 2nd solution (faster)
        def dfs_two(s, wordDict, memo):
            if len(s) == 0:
                return []
            if s in memo:
                return memo[s]

            results = []
            for word in wordDict:
                if not s.startswith(word): # Faster way to check
                    continue
                if len(s) == len(word):
                    results.append(s)
                else:
                    partitions = dfs(s[len(word):], wordDict, memo) # KEY: check the right part
                    for p in partitions:
                        results.append(word + " " + p)

            memo[s] = results # KEY: memo[s] = results, remember the results
            return results
        return dfs(s, wordDict, {})