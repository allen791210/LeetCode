class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        PARENTHESES = {")":"(", "]":"[", "}":"{"}
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if len(stack) == 0 or PARENTHESES[ch] != stack.pop(): # KEY: len(stack) == 0
                    return False
        
        return len(stack) == 0