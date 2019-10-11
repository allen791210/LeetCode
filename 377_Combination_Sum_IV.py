class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        results = []
        self.dfs_combinations(nums, target, )
        
    def 