"""
Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

Input: [[1,1],2,[1,1]]
Output: 10 

"""

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0

        depth = 1
        result = 0
        for i in nestedList:
            if isinstance(i, int):
                results += i * depth
            else:
                dfs_int(i, depth + 1)        
            
    def dfs_int(self, list, depth):
        num_sum = 0
        if isinstance(list, int):
            num_sum += list
        else:
            for n in range(len(list)):
                num_sum += self.dfs_int(n, depth + 1)
            
        return num_sum