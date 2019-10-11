"""
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if k == 0 or not s:
            return s
        
        stack = []
        for ch in s:
            if len(stack) > 0 and ch == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1]) # KEY: use stack and store "count" info
            
            while len(stack) > 0 and  stack[-1][1] >= k:
                if stack[-1][1] == k:
                    stack.pop()
                    while len(stack) > 2 and stack[-1][0] == stack[-2][0]:
                        stack[-2][1] += stack[-1][1]
                        stack.pop()
                else:
                    stack[-1][1] -= k

        return "".join([i*j for i, j in stack])