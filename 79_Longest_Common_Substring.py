"""
Example 1:
	Input:  "ABCD" and "CBCE"
	Output:  2
	
	Explanation:
	Longest common substring is "BC"
"""
"""
Example 1:
	Input:  "ABCD" and "CBCE"
	Output:  2
	
	Explanation:
	Longest common substring is "BC"
"""
"""
Example 1:
	Input:  "ABCD" and "CBCE"
	Output:  2
	
	Explanation:
	Longest common substring is "BC"
"""
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        if not A or not B:
            return 0
        
        longest_comm_string = 0
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)] # B: col, A: row
 
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 # Need to be continuous
                    longest_comm_string = max(longest_comm_string, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return longest_comm_string




