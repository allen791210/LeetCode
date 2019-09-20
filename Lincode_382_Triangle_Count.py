class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    """
    Input: [3, 4, 6, 7]
    Output: 3
    Explanation:
    They are (3, 4, 6), 
             (3, 6, 7),
             (4, 6, 7)
    """
    def triangleCount(self, S):
        S.sort()
        count = 0
        for i in range(len(S)):
            left = 0
            right = i - 1 # KEY: put right and left on the same side (a + b > c) => 容易有可以互相調整的規則
            while left < right:
                if S[left] + S[right] > S[i]:
                    count += right - left 
                    right -= 1
                else:
                    left += 1
        return count
            
