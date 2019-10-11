class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # KEY: palidrome string == reversed(string)
        t = s[::-1]
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)] # KEY: len + 1
        dp[0][0] = 0
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]: # index - 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return len(s) - dp[len(s)][len(t)] <= k