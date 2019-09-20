"""
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
"""
import collections

# KEY: counting way
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        #need = collections.Counter(s1)
        
        for i in s1:
            d1[i] += 1

        for j in s2[:len(s1)]:
            d2[j] += 1

        i, j = 0, len(s1)
        while j < len(s2):
            if d1 == d2:
                return True
            # remove first item
            d2[s2[i]] -= 1
            if d2[s2[i]] == 0:
                d2.pop(s2[i])
            # add next item
            d2[s2[j]] += 1
            i += 1; j += 1

        return d1 == d2
"""
"adc"
"dcda"
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) == 0 or len(s1) > len(s2):
            return False
        
        if len(s1) == 0:
            return True
        
        results = []
        visited = [False] * len(s1)
        self.dfs(s1, s2, visited, "", results)
        for p in results:
            if p in s2:
                return True
        
        return False

    def dfs(self, s1, s2, visited, permutation, results):
        if len(permutation) == len(s1):
            results.append(permutation)
            return
        
        for i in range(len(s1)):
            if not visited[i]:
                visited[i] = True
                self.dfs(s1, s2, visited, permutation + s1[i], results)
                visited[i] = False # remember resume

"""
CASE:
"prosperity"
"properties"
"""