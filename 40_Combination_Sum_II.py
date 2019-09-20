class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return [[]]
        # KEY STEP
        candidates = sorted(candidates)
        results = []
        self.dfs(candidates, target, 0, [], results)
        
        return results
    
    def dfs(self, candidates, target, start_idx, combinations, results):
        if target < 0:
            return
        
        if target == 0:
            results.append(list(combinations)) # deep copy, otherwise, combination.pop will alter the result.
        
        for i in range(start_idx, len(candidates)): # start_idx
            if i != start_idx and candidates[i - 1] == candidates[i]: # KEY: 因為candidates數字可重複 但答案不可重複 因此需要"去重"
                continue
            combinations.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i + 1, combinations, results)
            combinations.pop() # backtracking