class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return [[]]
        
        candidates = sorted(list(set(candidates))) # set -> remove duplicates
        combinations = []
        results = []
        self.dfs(candidates, target, 0, combinations, results)
        
        return results
    
    def dfs(self, candidates, target, start_idx, combinations, results):
        if target < 0:
            return
        
        if target == 0:
            results.append(list(combinations)) # deep copy, otherwise, combination.pop will alter the results as well.
        
        for i in range(start_idx, len(candidates)): # start from start_idx
            combinations.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combinations, results) # KEY: use "i", reuse the same number
            combinations.pop() # backtracking