# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if sol not in Solution.total_sol:
                Solution.total_sol.append(sol)
                return
            
        for i in range(start_idx, length):
            if candidates[i] > target:
                return
            self.DFS(candidates[i+1:], target-candidates[i], 0, sol+[candidates[i]])
            # sol 要注意不能讓其每次都重置一次，
            

#candidates = [10,1,2,7,6,1,5]
#target = 8
#candidates = [29,19,14,33,11,5,9,23,23,33,12,9,25,25,12,21,14,11,20,30,17,19,5,6,6,5,5,11,12,25,31,28,31,33,27,7,33,31,17,13,21,24,17,12,6,16,20,16,22,5]
#target = 28
#test = Solution()
#test.combinationSum2(candidates, target)
  