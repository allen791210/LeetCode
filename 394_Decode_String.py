"""
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # CANNOT use str e.g. "a"+"jk"+"c" e.g. "cjka" -> "akjc" WRONG
                tmp_s = []
                while stack and stack[-1] != '[':
                    tmp_s.append(stack.pop()) # KEY: pop makes order "reversed"
                stack.pop() # pop '['

                repeats, base = 0, 1
                while stack and stack[-1].isdigit():
                    repeats += (ord(stack.pop()) - ord('0')) * base # use ord()
                    base *= 10
                stack.append(''.join(reversed(tmp_s)) * repeats)

        return ''.join(stack)