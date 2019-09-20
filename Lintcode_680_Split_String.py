"""
Input: "123"
Output: [["1","2","3"],["12","3"],["1","23"]]
"""
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    def splitString(self, s):
        if not s:
            return []
        
        results = []
        self.dfs_split(s, 0, [], results)
        
        return results
    
    def dfs_split(self, s, start_idx, combinations, results):
        if start_idx == len(s):
            results.append(combinations)
            return
        
        # for i in range(start_idx, len(s)): # no need for loop because only 2 cases
        if start_idx + 1 <= len(s):
            self.dfs_split(s, start_idx + 1, combinations + s[start_idx:start_idx + 1], results ) # one element
        if start_idx + 2 <= len(s):
            self.dfs_split(s, start_idx + 2, combinations + s[start_idx:start_idx + 2], results ) # two elements






