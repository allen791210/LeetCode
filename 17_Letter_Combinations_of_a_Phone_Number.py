"""
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        results = []
        self.dfs(digits, 0, "", results)
        
        return results

    def dfs(self, digits, strat_idx, combinations, results):
        if len(combinations) == len(digits):
            results.append(combinations)
            return

        tmp_str = KEYBOARD[digits[strat_idx]]
        for i in range(len(tmp_str)):
            self.dfs(digits, strat_idx + 1, combinations + tmp_str[i], results)