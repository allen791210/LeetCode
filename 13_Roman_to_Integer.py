ROMAN_INT_DICT = { 
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    
}

class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        
        num_sum = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and ROMAN_INT_DICT[s[i]] < ROMAN_INT_DICT[s[i + 1]]:
                num_sum += (ROMAN_INT_DICT[s[i + 1]] - ROMAN_INT_DICT[s[i]])
                i += 2
            else:
                num_sum += ROMAN_INT_DICT[s[i]]
                i += 1
                
        return num_sum