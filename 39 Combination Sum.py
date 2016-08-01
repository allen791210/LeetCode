# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.total_sol = [] #將variable放在function裡面再test case的時候才會每次都重置(不能放外面)
        candidates.sort()
        self.DFS(candidates, target, 0, [])
        
        #print Solution.total_sol
        return Solution.total_sol
        
        
    def DFS(self, candidates, target, start_idx, sol):

        length = len(candidates)
        
        if target == 0:
            Solution.total_sol.append(sol)
            return
            
        for i in range(start_idx, length):
            if candidates[i] > target:
                return
            self.DFS(candidates, target-candidates[i], i, sol+[candidates[i]])
            # sol 要注意不能讓其每次都重置一次，
            # start_idx need to be changed to avoid repeated(same) solutions.

#test = Solution()
#test.combinationSum([2],1)