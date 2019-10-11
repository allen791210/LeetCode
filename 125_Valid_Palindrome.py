class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        tmp_str = ""
        for ch in s:
            if ch.isalpha() == True or ch.isnumeric() == True:
                tmp_str += ch

        tmp_str = tmp_str.lower()
        start, end = 0, len(tmp_str) - 1
        
        while start < end:
            if tmp_str[start] != tmp_str[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

s = Solution()
ss = "A man, a plan, a canal: Panama"
#ss = "0P"
print(s.isPalindrome(ss))